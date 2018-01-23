        self.single_word.clicked.connect(self.setText)
        self.file_input.clicked.connect(self.setOpenFileName)
        self.apply_encoding.clicked.connect(self.change_encoding)
        self.submit.clicked.connect(self.submit_clicked)
    
    def open_popup(self):
    	textLabel = QLabel()
    	textButton = QPushButton("QInputDialog.get&Text()")
    	print(textButton)
    	textButton.clicked.connect(self.setText)
    	
    def setText(self):
        self.progressBar.setProperty("value", 0)
        global given_input
        self.textBrowser.setText("")
        self.given_input.setText("")
        dialog=Dialog()
        if self.input_language_combo.currentIndex()==1:
        	text, ok = QInputDialog.getText(dialog, "ಪದ",
                "ಪರಿಶೀಲಿಸಲು ಬಯಸುವ ಪದ : ", QLineEdit.Normal,"")
        	if ok and text != '':
        		print(text)
        		provided_input="ದಾಖಲಿಸಿದ ಪದ : "+text
        		self.given_input.setText(provided_input)
        else:
        	text, ok = QInputDialog.getText(dialog, "Single word",
                "Enter the input:", QLineEdit.Normal,"")
        	if ok and text != '':           
        	    print(text)
        	    provided_input="The given input : "+text
        	    self.given_input.setText(provided_input)
        given_input=text
        
		
    def setOpenFileName(self):    
        options = QFileDialog.Options()
        self.progressBar.setProperty("value", 0)
        global given_input
        self.textBrowser.setText("")
        self.given_input.setText("")
        dialog=Dialog()
      
        fileName, _ = QFileDialog.getOpenFileName(dialog,
                "Select file", "",
                "Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
            provided_input="Input file : "+fileName
            self.given_input.setText(provided_input)
        given_input=fileName
       
    def change_encoding(self):
    #so current index 0= english
    #current index 1 is kannada
    #if kannada is selected, change everything to kannada
    	self.given_input.setText("")
    	self.textBrowser.setText("")
    	self.progressBar.setProperty("value", 0)
    	if self.input_language_combo.currentIndex()==1:
    		self.label.setText("ಪದ ಸಂಕೇತೀಕರಣವನ್ನು ಸೂಚಿಸಿ ")
    		self.input_language_combo.setItemText(0,"ಆಂಗ್ಲ")
    		self.input_language_combo.setItemText(1, "ಕನ್ನಡ")
    		self.label_2.setText("ಇವುಗಳಲ್ಲಿ ಒಂದು ಕಾರ್ಯವನ್ನು ಆಯ್ದುಕೊಳ್ಳಿರಿ : ")
    		self.radioButton_3.setText("ಪದ ಪರಿಶೀಲನೆ - ಸಂಧಿ ಛೇದದೊಡಗೂಡಿ")
    		self.radioButton_2.setText("ಸಂಧಿ ಛೇದ")
    		self.radioButton.setText("ಮೂಲ ಪದ ಉದ್ಧರಣ")
    		self.label_3.setText("ಪರಿಶೀಲಿಸಲು ಬಯಸುವ ಪದ :")
    		self.single_word.setText("ಪದ")
    		self.file_input.setText("ವಾಕ್ಯವೃಂದ")
    		self.submit.setText("ಸಲ್ಲಿಸು")
    		self.label_4.setText("ಫಲಿತಾಂಶ : ")
    		self.apply_encoding.setText("ಒಪ್ಪಿಸು")
    	else:
    		self.label.setText("Select Input Encoding: ")
    		self.input_language_combo.setItemText(0,"English")
    		self.input_language_combo.setItemText(1, "Kannada")
    		self.label_2.setText("Select Mode:")
    		self.radioButton_3.setText("Spell Checker with Sandhi Splitter")
    		self.radioButton_2.setText("Sandhi Splitter")
    		self.radioButton.setText("Root word extractor")
    		self.label_3.setText("Provide Input:")
    		self.single_word.setText("Single Word")
    		self.file_input.setText("File Input")
    		self.submit.setText("Submit")
    		self.label_4.setText("Output:")
    		self.apply_encoding.setText("Apply")
    		 #"ಪರಿಶೀಲಿಸಲು ಬಯಸುವ ಪದ : ", QLineEdit.Normal,"")
    def called_file(self,given_file_input,mode,prnt_res):
    #this is to handle the file cases.
    #taking three arguments, first to self, second input, third mode, fourt language
    	print("file called")
    	file_path=given_file_input.split('/')
    	file_name=file_path[-1]
    	in_file=open(file_name,"r")
    	file_write=""
    	ignored_words=[]
    	final_pratyaya=""
    	if prnt_res==3:
    	#stuffs are in kannada
    		if mode==1:
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					for sentence in sentences:
    						file_write+="\n"
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							words=sentence.split()
    							for word in words:
    								intact_word=word
    								after_pratyaya=pratyaya_chopper(word,3)
    								if after_pratyaya[0]==1:
    									word=to_uni(after_pratyaya[1])
    								if word in ignored_words:
    									file_write+=intact_word+" "
    									self.textBrowser.setText(file_write)
    									QApplication.processEvents()
    									continue
    								found_print=spell_check_kan(word)
    								if found_print[0]==1:
    									
    									file_write+=intact_word+" "
    									self.textBrowser.setText(file_write)
    									QApplication.processEvents()
    									
    								else:
    									if found_print[2]=="" or found_print[2]=='notthere':
    										dialog=Dialog()
    										
    									
    										text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ.\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ? ", QLineEdit.Normal,"")
    										if ok and text != '':
    											print(text)
    											add_success=add_word(text,3)
    								# 1 coz stuffs in english adn 3 for kan
    											if add_success==1:
    												QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												continue
    										else:
    											file_write+=intact_word+" "
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											continue
    									if len(found_print[2])>0:
    										dialog=Dialog()
    										ignore=["ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ", "ಸದಾ ಕಡೆಗಣಿಸಿ"]
    										#dialog.move(400,500)
    										item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ದೋಷಯುಕ್ತ  ಮೂಲ ಪದ : "+word+"\nನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ?  :",found_print[2]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)										
    										if ok and item:
    											selected=pick_selected(item,3)
    											print(selected)
    											if selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    												ignored_words.append(word)
    											if selected=="ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ" or selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    												file_write+=intact_word+" "
    												self.textBrowser.setText(file_write)
    												QApplication.processEvents()
    												continue
    											
    											if after_pratyaya[0]==1:
    												pratyayas=after_pratyaya[4]
    												pr_len=len(pratyayas)
    												i=1
    												while i<=pr_len:
    													pr=pratyayas[-i]
    													print("word is",word)
    													print("pr is",pr)
    													if len(pr)==1:
    														final_pratyaya+=pr
    													else:
    														final_pratyaya+=pr[:-1]
    													i=i+1
    												final_pratyaya+=pr[-1]
    												print("final pr",final_pratyaya)
    												print("prinintin pratyays")
    												print(pratyayas)
    												file_write+=to_uni(to_roman(selected)+final_pratyaya)+" "
    												final_pratyaya=""
    												
    											else:
    												file_write+=selected+" "
    											self.textBrowser.setText(file_write)
    											QApplication.processEvents()
    											
    										else:
    										#cancel is selected . no word is selected from suggestions
    											dialog=Dialog()
    											text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ  ", QLineEdit.Normal,"")
    											if ok and text != '':
    												print(text)
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												QApplication.processEvents()
    												add_success=add_word(text,3)
    							# 1 coz stuffs in english adn 3 for kan
    												if add_success==1:
    													QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    			
    			
    		elif mode==2:
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					sent_num=0
    					
    					for sentence in sentences:
    						sent_num+=1
    						nums=str(sent_num)
    						file_write+="\n["+nums+"] "+sentence+"\n"
    						self.textBrowser.setText(file_write)
    						self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    						QApplication.processEvents()
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							words=sentence.split()
    							words=list(set(words))
    							for word in words:
    								file_write+="\n"+word+" :\n"    								
    								after_pratyaya=pratyaya_chopper(word,3)
    								if after_pratyaya[0]==1:
    									word=to_uni(after_pratyaya[1])    									
    									file_write+=after_pratyaya[2]
    								
    								if word in ignored_words:
    									file_write+=word+" "
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    									continue
    								
    								if after_pratyaya[3]==1:
    									file_write+="ಈ ಪದವು ಪದಕೋಶದಲ್ಲಿ ಲಭ್ಯವಿದೆ! ಈ ಪದವು ಸಂದಿಪದವಲ್ಲದಿರಬಹುದು!\n"
    									continue
    								found_print=sandhi_splitter_kan(word)
    								if found_print[0]==1:
    									file_write+=found_print[1]    										
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    									
    								else:
    									if found_print[2]==0 or found_print[3]=="" or found_print[3]=='notthere':
    										dialog=Dialog()
    										
    									
    										text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ.\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ? ", QLineEdit.Normal,"")
    										if ok and text != '':
    											print(text)
    											add_success=add_word(text,3)
    								# 1 coz stuffs in english adn 3 for kan
    											if add_success==1:
    												QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												continue
    										else:
    											file_write+=word+" "
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											continue
    									if len(found_print[3])>0:
    										dialog=Dialog()
    										ignore=["ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ", "ಸದಾ ಕಡೆಗಣಿಸಿ"]
    										
    										item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ದೋಷಯುಕ್ತ ಮೂಲ ಪದ  : "+word+"\nನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ? ",found_print[3]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)										
    										if ok and item:
    											selected=pick_selected(item,1)
    											print(selected)
    											if selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    												ignored_words.append(word)
    											if selected=="ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ" or selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    												file_write+=word+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												continue
    											
    											
    											file_write+="ನೀವು ಆಯ್ದ ಪದ : "+selected+"\n "
    											found_print=sandhi_splitter_kan(selected)
    											file_write+=found_print[1]
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											
    										else:
    										#cancel is selected . no word is selected from suggestions
    											dialog=Dialog()
    											text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ?", QLineEdit.Normal,"")
    											if ok and text != '':
    												print(text)
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												add_success=add_word(text,3)
    							# 1 coz stuffs in english adn 3 for kan
    												if add_success==1:
    													QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    		elif mode==3:
    	#this is for kannada pratyaya chopper
    			sent_num=0
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					for sentence in sentences:
    						sent_num+=1
    						nums=str(sent_num)
    						file_write+="\n\n["+nums+"] "+sentence+"\n"
    						self.textBrowser.setText(file_write)
    						self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    						QApplication.processEvents()
    						file_write+="\n"
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							words=sentence.split()
    							words=list(set(words))
    							for word in words:
    								intact_word=word
    								file_write+="\n"+word+" :\n"   
    								after_pratyaya=pratyaya_chopper(word,3)
    								if after_pratyaya[0]==1:
    									word=to_uni(after_pratyaya[1])
    								if word in ignored_words:
    									file_write+=intact_word+" "
    									self.textBrowser.setText(file_write)
    									QApplication.processEvents()
    									continue
    								if after_pratyaya[3]==1:
    									file_write+="ಮೂಲ ಪದ  : "+to_uni(after_pratyaya[1])+"\n"
    									continue
    								else:
    								#check pratyaya has to_uni function in it
    									correct_selected=check_pratyaya(after_pratyaya[1],3)
    									print("cor",correct_selected[2])
    								
    									
    								if correct_selected[0]==1:    								
    									file_write+="\n"+after_pratyaya[2]+correct_selected[1]+"\n"
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    								elif correct_selected[2]=='' or correct_selected[2]=='notthere': 
    									dialog=Dialog()
    									file_write+=after_pratyaya[2]+word+" : ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ!\n"
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    									
    									text, ok = QInputDialog.getText(dialog,"ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ.\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ?", QLineEdit.Normal,"")
    									if ok and text != '':
    										print(text)
    										add_success=add_word(text,3)
    								# 1 coz stuffs in english adn 3 for kan
    										if add_success==1:
    											QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
		    	   				
    						
    								else:	
    									dialog=Dialog()
    									ignore=["ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ", "ಸದಾ ಕಡೆಗಣಿಸಿ"]							    											    					
    									item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ದೋಷಯುಕ್ತ ಮೂಲ ಪದ : "+word+"\nನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ? :", correct_selected[2]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)
    									if ok and item:
    										print(item)
    										selected=pick_selected(item,1)
    										if selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    											ignored_words.append(word)
    										if selected=="ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ" or selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    											file_write+="ಮೂಲ ಪದ : "+word+"\n "
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											continue
    										file_write+=after_pratyaya[2]+"ನೀವು ಆಯ್ದ ಮೂಲ ಪದ  : "+selected+"\n"
    										self.textBrowser.setText(file_write)
    										self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    										QApplication.processEvents()
    									else:
		    								
		    								dialog=Dialog()
		    								text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ  ", QLineEdit.Normal,"")
		    								if ok and text != '':
		    									print(text)
		    									add_success=add_word(text,3)
		    				# 1 coz stuffs in english
		    									if add_success==1:
		    										QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
		    			
		    #everything in english for file stuff		
    	else:
    		if mode==1:
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					for sentence in sentences:
    						file_write+="\n"
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							words=sentence.split()
    							for word in words:
    								intact_word=word
    								after_pratyaya=pratyaya_chopper(word,1)
    								if after_pratyaya[0]==1:
    									word=after_pratyaya[1]
    								if word in ignored_words:
    									file_write+=intact_word+" "
    									self.textBrowser.setText(file_write)
    									QApplication.processEvents()
    									continue
    								found_print=spell_check_eng(word)
    								if found_print[0]==1:
    									
    									file_write+=intact_word+" "
    									self.textBrowser.setText(file_write)
    									QApplication.processEvents()
    									
    								else:
    									if found_print[2]=="" or found_print[2]=='notthere':
    										dialog=Dialog()
    										
    									
    										text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available.\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    										if ok and text != '':
    											print(text)
    											add_success=add_word(text,1)
    								# 1 coz stuffs in english adn 3 for kan
    											if add_success==1:
    												QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												continue
    										else:
    											file_write+=intact_word+" "
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											continue
    									if len(found_print[2])>0:
    										dialog=Dialog()
    										ignore=["Ignore Once","Ignore All"]
    										#dialog.move(400,500)
    										item, ok = QInputDialog.getItem(dialog, "Suggestions","Mis-spelt root word : "+word+"\nDid you mean? :",found_print[2]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)										
    										if ok and item:
    											selected=pick_selected(item,1)
    											print(selected)
    											if selected=="Ignore All":
    												ignored_words.append(word)
    											if selected=="Ignore Once" or selected=="Ignore All":
    												file_write+=intact_word+" "
    												self.textBrowser.setText(file_write)
    												QApplication.processEvents()
    												continue
    											
    											if after_pratyaya[0]==1:
    												pratyayas=after_pratyaya[4]
    												pr_len=len(pratyayas)
    												i=1
    												while i<=pr_len:
    													pr=pratyayas[-i]
    													print("word is",word)
    													print("pr is",pr)
    													if len(pr)==1:
    														final_pratyaya+=pr
    													else:
    														final_pratyaya+=pr[:-1]
    													i=i+1
    												final_pratyaya+=pr[-1]
    												print("final pr",final_pratyaya)
    												print("prinintin pratyays")
    												print(pratyayas)
    												file_write+=selected+final_pratyaya+" "
    												final_pratyaya=""
    												
    											else:
    												file_write+=selected+" "
    											self.textBrowser.setText(file_write)
    											QApplication.processEvents()
    											
    										else:
    										#cancel is selected . no word is selected from suggestions
    											dialog=Dialog()
    											text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
    											if ok and text != '':
    												print(text)
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												QApplication.processEvents()
    												add_success=add_word(text,1)
    							# 1 coz stuffs in english adn 3 for kan
    												if add_success==1:
    													QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    			
    			
    		elif mode==2:
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					sent_num=0
    					
    					for sentence in sentences:
    						sent_num+=1
    						nums=str(sent_num)
    						file_write+="\n["+nums+"] "+sentence+"\n"
    						self.textBrowser.setText(file_write)
    						self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    						QApplication.processEvents()
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							words=sentence.split()
    							words=list(set(words))
    							for word in words:
    								file_write+="\n"+word+" :\n"    								
    								after_pratyaya=pratyaya_chopper(word,1)
    								if after_pratyaya[0]==1:
    									word=after_pratyaya[1]    									
    									file_write+=after_pratyaya[2]
    								
    								if word in ignored_words:
    									file_write+=word+" "
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    									continue
    								
    								if after_pratyaya[3]==1:
    									file_write+="The given word is present in the dictionary.The given word might not contain a sandhi!\n"
    									continue
    								found_print=sandhi_splitter_eng(word)
    								if found_print[0]==1:
    									file_write+=found_print[1]    										
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    									
    								else:
    									if found_print[2]==0 or found_print[3]=="" or found_print[3]=='notthere':
    										dialog=Dialog()
    										
    									
    										text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available.\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    										if ok and text != '':
    											print(text)
    											add_success=add_word(text,1)
    								# 1 coz stuffs in english adn 3 for kan
    											if add_success==1:
    												QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												continue
    										else:
    											file_write+=word+" "
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											continue
    									if len(found_print[3])>0:
    										dialog=Dialog()
    										ignore=["Ignore Once","Ignore All"]
    										
    										item, ok = QInputDialog.getItem(dialog, "Suggestions","Mis-spelt root word : "+word+"\nDid you mean? :",found_print[3]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)										
    										if ok and item:
    											selected=pick_selected(item,1)
    											print(selected)
    											if selected=="Ignore All":
    												ignored_words.append(word)
    											if selected=="Ignore Once" or selected=="Ignore All":
    												file_write+=word+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												continue
    											
    											
    											file_write+="You have selected : "+selected+"\n "
    											found_print=sandhi_splitter_eng(selected)
    											file_write+=found_print[1]
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											
    										else:
    										#cancel is selected . no word is selected from suggestions
    											dialog=Dialog()
    											text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
    											if ok and text != '':
    												print(text)
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												add_success=add_word(text,1)
    							# 1 coz stuffs in english adn 3 for kan
    												if add_success==1:
    													QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    		elif mode==3:
    	#this is for englisg pratyaya chopper
    			sent_num=0
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					for sentence in sentences:
    						sent_num+=1
    						nums=str(sent_num)
    						file_write+="\n\n["+nums+"] "+sentence+"\n"
    						self.textBrowser.setText(file_write)
    						self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    						QApplication.processEvents()
    						file_write+="\n"
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							words=sentence.split()
    							words=list(set(words))
    							for word in words:
    								intact_word=word
    								file_write+="\n"+word+" :\n"   
    								after_pratyaya=pratyaya_chopper(word,1)
    								if after_pratyaya[0]==1:
    									word=after_pratyaya[1]
    								if word in ignored_words:
    									file_write+=intact_word+" "
    									self.textBrowser.setText(file_write)
    									QApplication.processEvents()
    									continue
    								if after_pratyaya[3]==1:
    									file_write+="The root word is "+after_pratyaya[1]+"\n"
    									continue
    								else:
    									correct_selected=check_pratyaya(after_pratyaya[1],1)
    									print("cor",correct_selected[2])
    								
    									
    								if correct_selected[0]==1:    								
    									file_write+="\n"+after_pratyaya[2]+correct_selected[1]+"\n"
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    								elif correct_selected[2]=='' or correct_selected[2]=='notthere': 
    									dialog=Dialog()
    									file_write+=after_pratyaya[2]+"No Suggestions are generated for "+word+"\n"
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    									
    									text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available.\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    									if ok and text != '':
    										print(text)
    										add_success=add_word(text,1)
    								# 1 coz stuffs in english adn 3 for kan
    										if add_success==1:
    											QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
		    	   				
    						
    								else:	
    									dialog=Dialog()
    									ignore=["Ignore Once","Ignore All"]							    											    					
    									item, ok = QInputDialog.getItem(dialog, "Suggestions","Mis-spelt root word : "+word+"\nDid you mean? :", correct_selected[2]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)
    									if ok and item:
    										print(item)
    										selected=pick_selected(item,1)
    										if selected=="Ignore All":
    											ignored_words.append(word)
    										if selected=="Ignore Once" or selected=="Ignore All":
    											file_write+="The root word is "+word+"\n "
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											continue
    										file_write+=after_pratyaya[2]+"The correct root word is : "+selected+"\n"
    										self.textBrowser.setText(file_write)
    										self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    										QApplication.processEvents()
    									else:
		    								
		    								dialog=Dialog()
		    								text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
		    								if ok and text != '':
		    									print(text)
		    									add_success=add_word(text,1)
		    				# 1 coz stuffs in english
		    									if add_success==1:
		    										QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
		    			
		    					
    	#texteditor()
    	print("outside")
    	output_file=file_name[:-4]+"_out.txt"
    	out_file=open(output_file,"w")
    	out_file.write("%s\n" % file_write)
    	out_file.close()
    	dialog=Dialog()
    	#w=QWidget()
    	reply = QMessageBox.question(dialog, "Text Editor option","The file "+output_file+" is generated.\n Would you like to open it in an editor?" ,QMessageBox.Yes | QMessageBox.No)
    	
    	if reply == QMessageBox.Yes:
    		os.system("gedit "+output_file)
			
    def submit_clicked(self):
    	pb=0
    	add_success=0
    	after_chop_print=''
    	if given_input!="":

    		while pb<=100:
    			value = self.progressBar.value() + 1
    			self.progressBar.setProperty("value", value)
    			time.sleep(0.0000000001)
    			pb=value
    			#to update the GUI
    			QApplication.processEvents()
    			
    		#spell checker stuff	
    		if self.radioButton_3.isChecked():
    			
    			print("Spell checker selected")
    			if self.input_language_combo.currentIndex()==1:
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,1,3)
    				else:
    					to_chop_returned=pratyaya_chopper(given_input,3)
    		
    					if to_chop_returned[0]==1:
    							#self.textBrowser.setText(to_chop_returned[2])
    						correct_selected=spell_check_kan(to_uni(to_chop_returned[1]))
    						print("sent",to_chop_returned[1])
    						print("in elif returned to[2]",to_chop_returned[2])
    					else:   					  					
    					   	correct_selected=spell_check_kan(given_input)
    					print("cor",correct_selected[2])
    					if correct_selected[0]==1:
    						self.textBrowser.setText(to_chop_returned[2]+correct_selected[1]+"\nಸರಿಯಾದ ಪದ :"+given_input)
    				
    					elif correct_selected[2]=="" or correct_selected[2]=='notthere':
    						#no suggestions are generated
    						dialog=Dialog()
    						self.textBrowser.setText(to_chop_returned[2]+"ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ!!")
    						text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ.\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ? ", QLineEdit.Normal,"")
    						if ok and text != '':
    							print(text)
    							add_success=add_word(text,3)
    							# 1 coz stuffs in english adn 3 for kan
    						if add_success==1:
    							QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    					else:
    						dialog=Dialog()
    						print("correct_selected[2] is",correct_selected[2])
    						item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ? ", correct_selected[2], 0, False)
    						if ok and item:
    							print(item)
    							#3 because kannada
    							selected=pick_selected(item,3)
    							print(selected)
    							selected=to_roman(selected)
    							if to_chop_returned[0]==1:
    								pratyayas=to_chop_returned[4]
    								pr_len=len(pratyayas)
    								i=1
    								final_pratyaya=""
    								while i<=pr_len:
    									pr=pratyayas[-i]
    									
    									print("pr is",pr)
    									if len(pr)==1:
    										final_pratyaya+=pr
    									else:
    										final_pratyaya+=pr[:-1]
    									i=i+1
    								final_pratyaya+=pr[-1]
    								selected+=final_pratyaya
    								selected=to_uni(selected)
    							self.textBrowser.setText("ನೀವು ಆಯ್ದ ಸರಿಯಾದ ಪದ : "+selected)
    						else:
    						#cancel is selected . no word is selected from suggestions
    							dialog=Dialog()
    							text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ  ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,3)
    								# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    								QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    					
       			
        			
    			else:
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,1,1)
    				else:
    					to_chop_returned=pratyaya_chopper(given_input,0)
    					#need to improvise this and add changes to the kannada version as well
    					#this also seems to be fine!
    					if to_chop_returned[0]==1:
    						#self.textBrowser.setText(to_chop_returned[2])
    						correct_selected=spell_check_eng(to_chop_returned[1])
    						print("in elif returned to[2]",to_chop_returned[2])
    					else:   					  					
    					   	correct_selected=spell_check_eng(given_input)
    					if correct_selected[0]==1:
    						self.textBrowser.setText(to_chop_returned[2]+correct_selected[1])
    					
    					elif correct_selected[2]=="" or correct_selected[2]=='notthere':
    						#no suggestions are generated
    						dialog=Dialog()
    						self.textBrowser.setText(to_chop_returned[2]+"No Suggestions are generated!")
    						text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available.\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    						if ok and text != '':
    							print(text)
    							add_success=add_word(text,1)
    							# 1 coz stuffs in english adn 3 for kan
    						if add_success==1:
    							QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    					else:
    						dialog=Dialog()
    						print("correct_selected[2] is",correct_selected[2])
    						item, ok = QInputDialog.getItem(dialog, "Suggestions","Did you mean? :", correct_selected[2], 0, False)
    						if ok and item:
    							print(item)
    							#3 because kannada
    							selected=pick_selected(item,1)
    							print(selected)
    							if to_chop_returned[0]==1:
    								pratyayas=to_chop_returned[4]
    								pr_len=len(pratyayas)
    								i=1
    								final_pratyaya=""
    								while i<=pr_len:
    									pr=pratyayas[-i]
    									
    									print("pr is",pr)
    									if len(pr)==1:
    										final_pratyaya+=pr
    									else:
    										final_pratyaya+=pr[:-1]
    									i=i+1
    								final_pratyaya+=pr[-1]
    								selected+=final_pratyaya
    								
    							self.textBrowser.setText("The correct word is "+selected)
    						else:
    						#cancel is selected . no word is selected from suggestions
    							dialog=Dialog()
    							text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,1)
    								# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    								QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    					
    				
    				
    		#whole sandhi splitter stuff	
    		if self.radioButton_2.isChecked():
    			print("Sandhi splitter selected")
    			if self.input_language_combo.currentIndex()==1:
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,2,3)
    				else:
    					to_chop_returned=pratyaya_chopper(given_input,3)
    					#need to improvise this and add changes to the kannada version as well
    					#I guess everything is proper now. need to make a kannada version
    					print("inside")
    					if to_chop_returned[3]==1:
    						self.textBrowser.setText(to_chop_returned[2]+to_uni(to_chop_returned[1])+" : ಈ ಪದವು ಪದಕೋಶದಲ್ಲಿ ಲಭ್ಯವಿದೆ.\nಈ ಪದವು ಸಂದಿಪದವಲ್ಲದಿರಬಹುದು!")
    					else:
    						if to_chop_returned[0]==1:
    							found_print=sandhi_splitter_kan(to_uni(to_chop_returned[1]))
    							self.textBrowser.setText(to_chop_returned[2]+found_print[1])
    							print("in elif returned to[2]",to_chop_returned[2])
    						else:  
    							print("in else")  					  					
    							found_print=sandhi_splitter_kan(given_input)
    							self.textBrowser.setText(found_print[1])
    							
    						#print("found prnt 3 is",found_print[3])
    						print("length of found_prin",len(found_print))
    						if len(found_print)>2:
    							if found_print[4]==1:
    								print("found_print[4] ",found_print[4])
    								print("found_print[5] ",found_print[5])
    								print("found_print[3] ",found_print[3])
    								self.textBrowser.setText(found_print[5])
    								
#	
#	
    							
    						if len(found_print)>2:
    							if found_print[2]==1 and not (found_print[3]=='notthere' or found_print[3]==""):
    								dialog=Dialog()
    								print("that erros thisg",found_print[3])
    								item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ?", found_print[3], 0, False)
    								if ok and item:
    									print(item)
    									selected=pick_selected(item,3)
    									print(selected)
    									found_print=sandhi_splitter_kan(selected)
    									self.textBrowser.setText(found_print[1])
    								else:
		    							self.textBrowser.setText("")
		    							dialog=Dialog()
		    							text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ? : ", QLineEdit.Normal,"")
		    							if ok and text != '':
		    								print(text)
		    								add_success=add_word(text,3)
		    							# 1 coz stuffs in english
		    								if add_success==1:
		    									QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")				    		
    				
    						elif (len(found_print)<3 and found_print[0]!=1): #or (found_print[3]=='notthere' or found_print[3]==""):
		    					dialog=Dialog()
    							self.textBrowser.setText(to_chop_returned[2]+"ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ!!")
    							text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ.\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ? ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,3)
    								# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    								QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
		    
    				
    			else:
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,2,1)
    				else:
    					to_chop_returned=pratyaya_chopper(given_input,0)
    					#need to improvise this and add changes to the kannada version as well
    					#I guess everything is proper now. need to make a kannada version
    					print("inside")
    					if to_chop_returned[3]==1:
    						self.textBrowser.setText(to_chop_returned[2]+"\nThe word "+to_chop_returned[1]+" is present in the dictionary.\n It might not contain a sandhi!")
    					else:
    						if to_chop_returned[0]==1:
    							found_print=sandhi_splitter_eng(to_chop_returned[1])
    							self.textBrowser.setText(to_chop_returned[2]+found_print[1])
    							print("in elif returned to[2]",to_chop_returned[2])
    						else:    					  					
    							found_print=sandhi_splitter_eng(given_input)
    							self.textBrowser.setText(found_print[1])
    							print("in else")
    						#print("found prnt 3 is",found_print[3])
    						print("length of found_prin",len(found_print))
    						if len(found_print)>2:
    							if found_print[4]==1:
    								print("found_print[4] ",found_print[4])
    								print("found_print[5] ",found_print[5])
    								print("found_print[3] ",found_print[3])
    								self.textBrowser.setText(found_print[5])
    								
#	
#	
    							
    						if len(found_print)>2:
    							if found_print[2]==1 and not (found_print[3]=='notthere' or found_print[3]==""):
    								dialog=Dialog()
    								print("that erros thisg",found_print[3])
    								item, ok = QInputDialog.getItem(dialog, "Suggestions","Did you mean? :", found_print[3], 0, False)
    								if ok and item:
    									print(item)
    									selected=pick_selected(item,1)
    									print(selected)
    									found_print=sandhi_splitter_eng(selected)
    									self.textBrowser.setText(found_print[1])
    								else:
		    							self.textBrowser.setText("")
		    							dialog=Dialog()
		    							text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
		    							if ok and text != '':
		    								print(text)
		    								add_success=add_word(text,1)
		    							# 1 coz stuffs in english
		    								if add_success==1:
		    									QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")				    		
    				
    						elif (len(found_print)<3 and found_print[0]!=1): #or (found_print[3]=='notthere' or found_print[3]==""):
		    					dialog=Dialog()
    							self.textBrowser.setText(to_chop_returned[2]+"No Suggestions are generated!")
    							text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available.\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,1)
    								# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    								QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
		    
		    #for pratyaya chopper	   			
    		if self.radioButton.isChecked():
    			if self.input_language_combo.currentIndex()==1:
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,3,3)
    				else:
    					print("Root word extractor kannada selected")
    					after_pratyaya=pratyaya_chopper(given_input,3)
    					if after_pratyaya[0]==1:
    						self.textBrowser.setText(after_pratyaya[2])
    					if after_pratyaya[3]==0:
    						correct_selected=check_pratyaya(after_pratyaya[1],3)
    						print("cor",correct_selected[2])
    						if correct_selected[0]==1:
    							self.textBrowser.setText(after_pratyaya[2]+correct_selected[1])
    						elif correct_selected[2]=='' or correct_selected[2]=='notthere': 
    							dialog=Dialog()
    							self.textBrowser.setText(after_pratyaya[2]+"ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ!!")
    							text, ok = QInputDialog.getText(dialog,"ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ.\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ? ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,1)
    									# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    								QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
		    		   				
    							
    						else:	
    							dialog=Dialog()    					
    							item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ?:", correct_selected[2], 0, False)
    							if ok and item:
    								print(item)
    								selected=pick_selected(item,1)
    								print("after")
    								print(after_pratyaya[2])
    								self.textBrowser.setText(after_pratyaya[2]+"\nಸರಿಯಾದ ಮೂಲ ಪದ : "+selected)
    							else:
		    						self.textBrowser.setText("")
		    						dialog=Dialog()
		    						text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ : ", QLineEdit.Normal,"")
		    						if ok and text != '':
		    							print(text)
		    							add_success=add_word(text,1)
		    					# 1 coz stuffs in english
		    							if add_success==1:
		    								QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
		    			
    			else:
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,3,1)
    				else:
    					print("Root word extractor selected")
    					after_pratyaya=pratyaya_chopper(given_input,1)
    					if after_pratyaya[0]==1:
    						self.textBrowser.setText(after_pratyaya[2])
    					if after_pratyaya[3]==0:
    						correct_selected=check_pratyaya(after_pratyaya[1],1)
    						print("cor",correct_selected[2])
    						if correct_selected[0]==1:
    							self.textBrowser.setText(after_pratyaya[2]+correct_selected[1])
    						elif correct_selected[2]=='' or correct_selected[2]=='notthere': 
    							dialog=Dialog()
    							self.textBrowser.setText(after_pratyaya[2]+"No Suggestions are generated!")
    							text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available.\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,1)
    									# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    								QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
		    		   				
    							
    						else:	
    							dialog=Dialog()    					
    							item, ok = QInputDialog.getItem(dialog, "Suggestions","Did you mean? :", correct_selected[2], 0, False)
    							if ok and item:
    								print(item)
    								selected=pick_selected(item,1)
    								self.textBrowser.setText(after_pratyaya[2]+"\nThe correct root word is : "+selected)
    							else:
		    						self.textBrowser.setText("")
		    						dialog=Dialog()
		    						text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
		    						if ok and text != '':
		    							print(text)
		    							add_success=add_word(text,1)
		    					# 1 coz stuffs in english
		    							if add_success==1:
		    								QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
		    			
		    				
    			
    	else:
    		dialog=Dialog()
    		if self.input_language_combo.currentIndex()==1:
    			reply = QMessageBox.information(dialog,"ಸೂಚನೆ", "ದಯಮಾಡಿ ಪರಿಶೀಲಿಸ ಬಯಸುವ ಪದವನ್ನು ದಾಖಲಿಸಿ")
    		else:
    			reply = QMessageBox.information(dialog,"Information", "Please provide a valid input")
   
   
   	
             
class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.move(400,150)
    



