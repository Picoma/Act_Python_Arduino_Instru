# Bibliothèque de fonctions spécifiques au TP utilisé.

from matplotlib import pyplot as plt
from matplotlib.widgets import Cursor
import numpy as np

def transforme_message_arduino(line):
    while line[0] == "A":
        line = line[1:] # Vire les A issus de l'abscence de communication
        
    t,Uc=line.split(";")
    t=float(t)*1e-3
    Uc=float(Uc)*5/1024
    return(t,Uc)

def fait_un_joli_graphique():
    plt.grid()
    plt.xlabel("Temps (s)")
    plt.ylabel("Tension Uc (V)")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.legend()

# From https://matplotlib.org/stable/gallery/event_handling/cursor_demo.html#snapping-to-data-points
class SnappingCursor(Cursor):    
    def __init__(self, ax, line, horizOn=True, vertOn=True, useblit=False, **lineprops):
        super().__init__(ax, horizOn=horizOn, vertOn=vertOn, useblit=useblit, **lineprops)
        self._last_index = None
        self.x, self.y = line.get_data()
        self.text = ax.text(0.72, 0.9, '', transform=ax.transAxes)
    
    def onmove(self, event):
        """Internal event handler to draw the cursor when the mouse moves."""
        if self.ignore(event):
            self._last_index = None
            return
        if not self.canvas.widgetlock.available(self):
            self._last_index = None
            return
        if event.inaxes != self.ax:
            self.linev.set_visible(False)
            self.lineh.set_visible(False)
            self._last_index = None

            if self.needclear:
                self.canvas.draw()
                self.needclear = False
            return
        self.needclear = True
        if not self.visible:
            self._last_index = None
            return
        
        x, y = event.xdata, event.ydata
        index = min(np.searchsorted(self.x, x), len(self.x) - 1)
        if index == self._last_index:
            return  # still on the same data point. Nothing to do.
        self._last_index = index
        x = self.x[index]
        y = self.y[index]
        # update the line positions
        self.lineh.set_ydata((y,y))
        self.linev.set_xdata((x,x))
        self.text.set_text('x=%1.2f, y=%1.2f' % (x, y))
        self.ax.figure.canvas.draw()
        
        self.linev.set_visible(self.visible and self.vertOn)
        self.lineh.set_visible(self.visible and self.horizOn)

        self._update()