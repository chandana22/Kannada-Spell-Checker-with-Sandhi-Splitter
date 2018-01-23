#!/usr/bin/env python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

from PyQt5.QtCore import (pyqtProperty, QDirIterator, QEasingCurve, QEvent,
        QEventTransition, QHistoryState, QParallelAnimationGroup, QPointF,
        QPropertyAnimation, QRectF, QSequentialAnimationGroup, QSize, QState,
        QStateMachine, Qt)
from PyQt5.QtGui import (QBrush, QColor, QFont, QLinearGradient, QPainter,
        QPalette, QPen, QPixmap, QTransform)
from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsObject,
        QGraphicsProxyWidget, QGraphicsRotation, QGraphicsScene, QGraphicsView,
        QKeyEventTransition, QWidget)
from PyQt5.QtOpenGL import QGL, QGLFormat, QGLWidget

import padnavigator_rc
from ui_form import Ui_Form

class PadNavigator(QGraphicsView):
    def __init__(self, size, parent=None):
        super(PadNavigator, self).__init__(parent)

        self.form = Ui_Form()		
		
        splash = SplashItem()
        splash.setZValue(1)

        pad = FlippablePad(size)
        flipRotation = QGraphicsRotation(pad)
        xRotation = QGraphicsRotation(pad)
        yRotation = QGraphicsRotation(pad)
        flipRotation.setAxis(Qt.YAxis)
        xRotation.setAxis(Qt.YAxis)
        yRotation.setAxis(Qt.XAxis)
        pad.setTransformations([flipRotation, xRotation, yRotation])

        backItem = QGraphicsProxyWidget(pad)
        widget = QWidget()
        #setting up the form fields
        #widget is form?
        self.form.setupUi(widget)
        #self.form.hostName.setFocus()
        #self_form=ConfigDialog()
        #connectwigs(widget)
        
        backItem.setWidget(widget)
        backItem.setVisible(False)
        backItem.setFocus()
        backItem.setCacheMode(QGraphicsItem.ItemCoordinateCache)
        r = backItem.rect()
        backItem.setTransform(QTransform().rotate(180, Qt.YAxis).translate(-r.width()/2, -r.height()/2))

	#making it zero removed the numbers
        selectionItem = RoundRectItem(QRectF(0, 0,0,0),
                QColor(Qt.white), pad)
        selectionItem.setZValue(0.5)

        smoothSplashMove = QPropertyAnimation(splash, "y")
        smoothSplashOpacity = QPropertyAnimation(splash, "opacity")
        smoothSplashMove.setEasingCurve(QEasingCurve.InQuad)
        smoothSplashMove.setDuration(250)
        smoothSplashOpacity.setDuration(250)

        smoothXSelection = QPropertyAnimation(selectionItem, "x")
        smoothYSelection = QPropertyAnimation(selectionItem, "y")
        smoothXRotation = QPropertyAnimation(xRotation, "angle")
        smoothYRotation = QPropertyAnimation(yRotation, "angle")
        smoothXSelection.setDuration(125)
        smoothYSelection.setDuration(125)
        smoothXRotation.setDuration(125)
        smoothYRotation.setDuration(125)
        smoothXSelection.setEasingCurve(QEasingCurve.InOutQuad)
        smoothYSelection.setEasingCurve(QEasingCurve.InOutQuad)
        smoothXRotation.setEasingCurve(QEasingCurve.InOutQuad)
        smoothYRotation.setEasingCurve(QEasingCurve.InOutQuad)

        smoothFlipRotation = QPropertyAnimation(flipRotation, "angle")
        smoothFlipScale = QPropertyAnimation(pad, "scale")
        smoothFlipXRotation = QPropertyAnimation(xRotation, "angle")
        smoothFlipYRotation = QPropertyAnimation(yRotation, "angle")
        flipAnimation = QParallelAnimationGroup(self)
        smoothFlipScale.setDuration(500)
        smoothFlipRotation.setDuration(500)
        smoothFlipXRotation.setDuration(500)
        smoothFlipYRotation.setDuration(500)
        smoothFlipScale.setEasingCurve(QEasingCurve.InOutQuad)
        smoothFlipRotation.setEasingCurve(QEasingCurve.InOutQuad)
        smoothFlipXRotation.setEasingCurve(QEasingCurve.InOutQuad)
        smoothFlipYRotation.setEasingCurve(QEasingCurve.InOutQuad)
        smoothFlipScale.setKeyValueAt(0, 1.0)
        smoothFlipScale.setKeyValueAt(0.5, 0.7)
        smoothFlipScale.setKeyValueAt(1, 1.0)
        flipAnimation.addAnimation(smoothFlipRotation)
        flipAnimation.addAnimation(smoothFlipScale)
        flipAnimation.addAnimation(smoothFlipXRotation)
        flipAnimation.addAnimation(smoothFlipYRotation)

        setVariablesSequence = QSequentialAnimationGroup()
        setFillAnimation = QPropertyAnimation(pad, "fill")
        setBackItemVisibleAnimation = QPropertyAnimation(backItem, "visible")
        setSelectionItemVisibleAnimation = QPropertyAnimation(selectionItem, "visible")
        setFillAnimation.setDuration(0)
        setBackItemVisibleAnimation.setDuration(0)
        setSelectionItemVisibleAnimation.setDuration(0)
        setVariablesSequence.addPause(250)
        setVariablesSequence.addAnimation(setBackItemVisibleAnimation)
        setVariablesSequence.addAnimation(setSelectionItemVisibleAnimation)
        setVariablesSequence.addAnimation(setFillAnimation)
        flipAnimation.addAnimation(setVariablesSequence)

        stateMachine = QStateMachine(self)
        splashState = QState(stateMachine)
        frontState = QState(stateMachine)
        historyState = QHistoryState(frontState)
        backState = QState(stateMachine)

        frontState.assignProperty(pad, "fill", False)
        frontState.assignProperty(splash, "opacity", 0.0)
        frontState.assignProperty(backItem, "visible", False)
        frontState.assignProperty(flipRotation, "angle", 0.0)
        frontState.assignProperty(selectionItem, "visible", True)

        backState.assignProperty(pad, "fill", True)
        backState.assignProperty(backItem, "visible", True)
        backState.assignProperty(xRotation, "angle", 0.0)
        backState.assignProperty(yRotation, "angle", 0.0)
        backState.assignProperty(flipRotation, "angle", 180.0)
        backState.assignProperty(selectionItem, "visible", False)

        stateMachine.addDefaultAnimation(smoothXRotation)
        stateMachine.addDefaultAnimation(smoothYRotation)
        stateMachine.addDefaultAnimation(smoothXSelection)
        stateMachine.addDefaultAnimation(smoothYSelection)
        stateMachine.setInitialState(splashState)

        anyKeyTransition = QEventTransition(self, QEvent.KeyPress, splashState)
        anyKeyTransition.setTargetState(frontState)
        anyKeyTransition.addAnimation(smoothSplashMove)
        anyKeyTransition.addAnimation(smoothSplashOpacity)

        enterTransition = QKeyEventTransition(self, QEvent.KeyPress,
                Qt.Key_Enter, backState)
        returnTransition = QKeyEventTransition(self, QEvent.KeyPress,
                Qt.Key_Return, backState)
        backEnterTransition = QKeyEventTransition(self, QEvent.KeyPress,
                Qt.Key_Enter, frontState)
        backReturnTransition = QKeyEventTransition(self, QEvent.KeyPress,
                Qt.Key_Return, frontState)
        enterTransition.setTargetState(historyState)
        returnTransition.setTargetState(historyState)
        backEnterTransition.setTargetState(backState)
        backReturnTransition.setTargetState(backState)
        enterTransition.addAnimation(flipAnimation)
        returnTransition.addAnimation(flipAnimation)
        backEnterTransition.addAnimation(flipAnimation)
        backReturnTransition.addAnimation(flipAnimation)

        columns = 1 
        #size.width()
        rows = 1 
        #size.height()
        stateGrid = []
        for y in range(rows):
            stateGrid.append([QState(frontState) for _ in range(columns)])

        frontState.setInitialState(stateGrid[0][0])
        selectionItem.setPos(pad.iconAt(0, 0).pos())

        for y in range(rows):
            for x in range(columns):
                state = stateGrid[y][x]

                rightTransition = QKeyEventTransition(self, QEvent.KeyPress,
                        Qt.Key_Right, state)
                leftTransition = QKeyEventTransition(self, QEvent.KeyPress,
                        Qt.Key_Left, state)
                downTransition = QKeyEventTransition(self, QEvent.KeyPress,
                        Qt.Key_Down, state)
                upTransition = QKeyEventTransition(self, QEvent.KeyPress,
                        Qt.Key_Up, state)

                rightTransition.setTargetState(stateGrid[y][(x + 1) % columns])
                leftTransition.setTargetState(stateGrid[y][((x - 1) + columns) % columns])
                downTransition.setTargetState(stateGrid[(y + 1) % rows][x])
                upTransition.setTargetState(stateGrid[((y - 1) + rows) % rows][x])

                icon = pad.iconAt(x, y)
                state.assignProperty(xRotation, "angle", -icon.x() / 6.0)
                state.assignProperty(yRotation, "angle", icon.y() / 6.0)
                state.assignProperty(selectionItem, "x", icon.x())
                state.assignProperty(selectionItem, "y", icon.y())
                frontState.assignProperty(icon, "visible", True)
                backState.assignProperty(icon, "visible", False)

                setIconVisibleAnimation = QPropertyAnimation(icon, "visible")
                setIconVisibleAnimation.setDuration(0)
                setVariablesSequence.addAnimation(setIconVisibleAnimation)

        scene = QGraphicsScene(self)
        scene.setBackgroundBrush(QBrush(QPixmap(":/images/7.2.111.jpg")))
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        scene.addItem(pad)
        scene.setSceneRect(scene.itemsBoundingRect())
        self.setScene(scene)

        sbr = splash.boundingRect()
        splash.setPos(-sbr.width() / 2, scene.sceneRect().top() - 2)
        frontState.assignProperty(splash, "y", splash.y() - 100.0)
        scene.addItem(splash)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setMinimumSize(50, 50)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setRenderHints(QPainter.Antialiasing |
                QPainter.SmoothPixmapTransform | QPainter.TextAntialiasing)

        if QGLFormat.hasOpenGL():
            self.setViewport(QGLWidget(QGLFormat(QGL.SampleBuffers)))

        stateMachine.start()

    def resizeEvent(self, event):
        super(PadNavigator, self).resizeEvent(event)
        self.fitInView(self.scene().sceneRect(), Qt.KeepAspectRatio)


class RoundRectItem(QGraphicsObject):
    def __init__(self, bounds, color, parent=None):
        super(RoundRectItem, self).__init__(parent)

        self.fillRect = False
        self.bounds = QRectF(bounds)
        self.pix = QPixmap()

        self.gradient = QLinearGradient()
        self.gradient.setStart(self.bounds.topLeft())
        self.gradient.setFinalStop(self.bounds.bottomRight())
        self.gradient.setColorAt(0, color)
        self.gradient.setColorAt(1, color.darker(200))

        self.setCacheMode(QGraphicsItem.ItemCoordinateCache)

    def setFill(self, fill):
        self.fillRect = fill
        self.update()

    def fill(self):
        return self.fillRect

    fill = pyqtProperty(bool, fill, setFill)

    def paint(self, painter, option, widget):
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 0, 0))
        painter.drawRoundedRect(self.bounds.translated(2, 2), 25.0, 25.0)

        if self.fillRect:
            painter.setBrush(QApplication.palette().brush(QPalette.Window))
        else:
            painter.setBrush(self.gradient)

        painter.setPen(QPen(Qt.black, 1))
        painter.drawRoundedRect(self.bounds, 25.0, 25.0)
        if not self.pix.isNull():
            painter.scale(1.95, 1.95)
            painter.drawPixmap(-self.pix.width() / 2, -self.pix.height() / 2, self.pix)

    def boundingRect(self):
        return self.bounds.adjusted(0, 0, 0, 0)

    def pixmap(self):
        return QPixmap(self.pix)

    def setPixmap(self, pixmap):
        self.pix = QPixmap(pixmap)
        self.update()


class FlippablePad(RoundRectItem):
    def __init__(self, size, parent=None):
        super(FlippablePad, self).__init__(self.boundsFromSize(size),
                QColor(6, 5, 2, 4), parent)

        #numIcons = size.width() * size.height()
        numIcons=1
        pixmaps = []
        it = QDirIterator(":/images", ["*.png"])
        while it.hasNext() and len(pixmaps) < numIcons:
            pixmaps.append(it.next())

        iconRect = QRectF(-600,-600, 1200, 1200)
        iconColor = QColor(0,0,0,0)
        self.iconGrid = []
        n = 0

        for y in range(size.height()):
            row = []

            for x in range(size.width()):
                rect = RoundRectItem(iconRect, iconColor, self)
                rect.setZValue(1)
                rect.setPos(self.posForLocation(x, y, size))
                rect.setPixmap(pixmaps[n % len(pixmaps)])
                n += 1

                row.append(rect)

            self.iconGrid.append(row)

    def iconAt(self, column, row):
        return self.iconGrid[row][column]

    @staticmethod
    def boundsFromSize(size):
        return QRectF((-size.width() / 2.0) * 150,
                (-size.height() / 2.0) * 150, size.width() * 150,
                size.height() * 150)

    @staticmethod
    def posForLocation(column, row, size):
        return QPointF(column * 150, row * 150) - QPointF((size.width() - 1) * 75, (size.height() - 1) * 75)


class SplashItem(QGraphicsObject):
    def __init__(self, parent=None):
        super(SplashItem, self).__init__(parent)

        self.text = " Welcome! Press Enter key to begin."

        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

    def boundingRect(self):
        return QRectF(0, 0, 320, 40)

    def paint(self, painter, option, widget):
        painter.setPen(QPen(Qt.black, 2))
        painter.setBrush(QColor(245, 245, 255, 220))
        painter.setClipRect(self.boundingRect())
        painter.drawRoundedRect(3, -100 + 3, 400 - 6, 250 - 6, 25.0, 25.0)

        textRect = self.boundingRect().adjusted(10, 10, -10, -10)
        flags = int(Qt.AlignTop | Qt.AlignLeft) | Qt.TextWordWrap

        font = QFont()
        font.setPixelSize(18)
        painter.setPen(Qt.black)
        painter.setFont(font)
        painter.drawText(textRect, flags, self.text)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    navigator = PadNavigator(QSize(1,1))
    navigator.show()

    sys.exit(app.exec_())
