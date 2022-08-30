#define TRUE 1

class Array {
    public:
        AntElm Elms[][];   /* Array of antenna elements */

	void steerArray(int xmin, int xmax, int ymin, int ymax, double az, double el, int wavelength) {
	    if(xmin<xmax) {
	        steerArray(xmin,(xmax-xmin)/2,ymin,(ymax-ymin)/2,az,el,wavelength);
	        steerArray((xmax-xmin)/2+1,xmax,(ymax-ymin)/2+1,ymax,az,el,wavelength);
	    } else {
	        (*this).Elm[xmin][ymin].w.setPhase(xmin,ymin,az,el,wavelength);
	        (*this).Elm[xmin][ymin].lock = TRUE;
	    }
        }

	void windowFn() {
	    /* Gaussian */
	    /* Hamming */
	    /* Blackman-Harris */
        }
};

