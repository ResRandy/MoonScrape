# from tkinter import *
import tkinter as tk
# from tkinter import ttk
# from tkinter.ttk import Style

# import platform

from moon_scrape_home import Moon_Scrape_Home_Page
from moon_scrape_doc_to_excel import Doc_To_Excel_Moon_Scrape_Page
from moon_scrape_excel_to_excel import Excel_To_Excel_Moon_Scrape_Page
from moon_scrape_excel_to_sheet import Excel_To_Sheet_Moon_Scrape_Page


"""
	The following code has been added by Randolph Stokes 3/17/26.
	This is just an app that is supposed to run the home page by itself.

"""
class Moon_Scrape_app(tk.Tk):

	def __init__(self, *args, **kwargs):
		# LARGE_FONT = ('Bell Gothic Std Black', 40, 'bold')
		# MEDIUM_FONT = ('Bell Gothic Std Black', 25, 'bold')
		# BUTTON_FONT = ('Calibiri', 14, 'bold')
		BACKGROUND_COLOR = '#407297'
		# LIGHT_BLUE = '#d4e1fa'

		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self, 'Moon Scrape')
		tk.Tk.wm_geometry(self, '1440x810') 


		self.protocol('WM_DELETE_WINDOW', lambda : \
                      self.close_application())
		
		# os_name = platform.system()
		# if os_name == 'Windows':
		# 	self.state('zoomed')
		# 	self.isFullScreen = False
		# elif os_name == 'Darwin':
		# 	self.attributes('-fullscreen', True)
		# 	self.isFullScreen = False
		# else:
		# 	self.attributes('-fullscreen', True)
		# 	self.isFullScreen = True
		
		# self.bind('<Escape>', self.toggle_fullscreen)
		self.minsize(400, 300)
	

		container = tk.Frame(self)
		container.pack(side="top",fill="both")
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.container_please = container
		self.spreadsheet_path = ''
		self.frames = {}
		self.df = []
		self.sheet_index = 0
		self.sheet_name = ''
		self.selected_sheet = False
		self.submit_selection = False

		for F in (Moon_Scrape_Home_Page, Excel_To_Excel_Moon_Scrape_Page,Excel_To_Sheet_Moon_Scrape_Page, Doc_To_Excel_Moon_Scrape_Page):
			frame = F(container, self)
			frame.config(bg=BACKGROUND_COLOR)
			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky=tk.NSEW)
        
		self.show_frame(Moon_Scrape_Home_Page)

	
	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()

	

	def close_application(self):
		"""
        Method called when the app is closed. Cloases any open spreadsheets.
        """

		if hasattr(self, 'sheet'):
			self.sheet.close(self)
		self.destroy()

	def run(self):
		self.mainloop()

Moon_Scrape_app().run()