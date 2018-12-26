import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

SELECT_SENSITIVITY = 0.01

class Annotate(object):
    def __init__(self):
	self.is_pressed = False
        self.ax = plt.gca()
        self.rect = Rectangle((0,0), 1, 1, fill=None, alpha=1,linewidth=1,edgecolor='r', linestyle='dashed')
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
	self.senseRects()
        self.ax.add_patch(self.rect)
        self.ax.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.ax.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.ax.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def senseRects(self):
	self.corners = {}
	if self.x0 < self.x1:
	    x0 = self.x0
	    x1 = self.x1
	else:
	    x0 = self.x1
	    x1 = self.x0
	if self.y0 < self.y1:
	    y0 = self.y0
	    y1 = self.y1
	else:
	    y0 = self.y1
	    y1 = self.y0	
	    
	for cn,point in [('LB',(x0, y0)),
			 ('LT',(x0, y1)),
			 ('RT',(x1, y1)),
			 ('RB',(x1, y0))]:
	    x,y = point
	    self.corners[cn] = (x-SELECT_SENSITIVITY, y-SELECT_SENSITIVITY,
				 x+SELECT_SENSITIVITY, y+SELECT_SENSITIVITY)

    def getProximity(self, event):
	x = event.xdata
	y = event.ydata
	print "E:",x,y
	for cn in ['LT','LB','RB','RT']:
	    x0,y0,x1,y1 = self.corners[cn]
	    print "P %s>"%cn,x0,y0,x1,y1
	    if (x0<=x<=x1) and (y0<=y<=y1):
		print "P> ",cn
		return cn
	else:
	    print "P> None"
	    return None
	

    def on_press(self, event):
        print 'press'
	if not event.inaxes: return
	self.corner = self.getProximity(event)
	if self.corner:
	    # Change cursor accordingly
	    self.is_pressed = True
	    self.xc = event.xdata
	    self.yc = event.ydata
	    self.rect.set_width(self.xc - self.x0)
	    self.rect.set_height(self.yc - self.y0)
	    self.rect.set_xy((self.x0, self.y0))
	    self.ax.figure.canvas.draw()
	else:
	    self.is_pressed = True
	    self.x0 = event.xdata
	    self.y0 = event.ydata
	    
    def on_motion(self, event):
	if not event.inaxes: return	
	if self.is_pressed:
	    if not self.corner:
		self.xc = event.xdata
		self.yc = event.ydata
		self.rect.set_width(self.xc - self.x0)
		self.rect.set_height(self.yc - self.y0)
		self.rect.set_xy((self.x0, self.y0))
		#self.senseRects()
		self.ax.figure.canvas.draw()
	    else:
		if self.corner == 'LT':
		    self.x0 = event.xdata
		    self.y0 = event.ydata
		    self.rect.set_width(self.x1 - self.x0)
		    self.rect.set_height(self.y1 - self.y0)
		elif self.corner == 'LB':
		    self.x0 = event.xdata
		    self.yc = event.ydata
		    self.rect.set_width(self.x1 - self.x0)
		    self.rect.set_height(self.yc - self.y0)
		elif self.corner == 'RT':
		    self.xc = event.xdata
		    self.y0 = event.ydata
		    self.rect.set_width(self.xc - self.x0)
		    self.rect.set_height(self.y1 - self.y0)	    
		elif self.corner == 'RB':
		    self.xc = event.xdata
		    self.yc = event.ydata
		    self.rect.set_width(self.xc - self.x0)
		    self.rect.set_height(self.yc - self.y0)
		self.rect.set_xy((self.x0, self.y0))
		#self.senseRects()
		self.ax.figure.canvas.draw()
	else:
	    corner = self.getProximity(event)
	    if corner:
		print "*",
	
    def on_release(self, event):
        print 'release'
	self.is_pressed = False
        self.x1 = event.xdata
        self.y1 = event.ydata
        self.rect.set_width(self.x1 - self.x0)
        self.rect.set_height(self.y1 - self.y0)
        self.rect.set_xy((self.x0, self.y0))
	self.senseRects()
        

a = Annotate()
plt.show()
