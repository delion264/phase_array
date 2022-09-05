#include <vector>

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

        double getPhase(std::vector<int> elm_index) {
            return (*this).Elm[elm_index(0)][elm_index(1)].w.relativePhase();
        }

        std::vector<double> directionFind() {
            /*
                Obtains relative phases for all elements using getPhase() and uses this to set up
                a system of linear equations to solve for the angle of arrival
                (φ,θ). 
            */
        }
};
