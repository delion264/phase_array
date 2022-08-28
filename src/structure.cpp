class WaveVector {
    public:
        double az;
        double el;
        double phase;   /* in rads */
        int wavelength; /* in Hertz */
};

class AntElm {
    public:
        int row;
        int col;
        WaveVector w;
        bool lock;      /* indicates if array element is in use */

        void setPhase(double az, double el, int wavelength);
};

class Array {
    public:
        void steerArray();
        void setWavelength();
        AntElm *Elms[][];   /* Array of antenna elements */
};

class SubArray : public Array {
    /* Implements Uniform Rectangular subarray */
};

/*  
    Calculates phase offset applied to antenna element (p,q) given 
    a transmit direction or DoA in spherical coordinates (az,el) === (φ,θ) 
    and the transmit wavelength λ.
    Actual phase offset is given by ψ = (-2*π*(p-1)*d/λ)*u
    E-field contribution is given by taking exp(i*ψ).
*/
void AntElm::setPhase(double az, double el, int wavelength) {
    int p = self.row;
    int q = self.col;
    double u, v, wx, wy, s_phase;

    u = sin(el)*cos(az);
    v = sin(el)*sin(az);
    wx = -2*pi*i*(p - 1)*d/wavelength*u;
    wy = -2*pi*i*(q - 1)*d/wavelength*v;

    self.phase = wx + wy;                  /* Steering phase */
}

/* Divide and conquer method to avoid nested loops. Implementation needs to be checked. */
void Array::steerArray(int xmin, int xmax, int ymin, int ymax, double az, double el, int wavelength) {
    if(xmin<xmax) {
        steerArray(0,(xmax-xmin)/2,0,(ymax-ymin)/2,az,el,wavelength);
        steerArray((xmax-xmin)/2+1,xmax,(ymax-ymin)/2+1,ymax,az,el,wavelength);
    } else {
        self.Elm[xmin][ymin].setPhase(az,el,wavelength);
    }
}

/*
    arrayFactor() might be superfluous for transmit applications but
    may be needed for DoA application.
    Potential approach:

    1) Calculate cross correlation of all elements with respect to a
    reference signal to obtain phase differences across all antenna 
    elements

    2) Use the above result to obtain a system of linear equations to 
    solve for φ and θ
*/
double arrayFactor(int p, int q, double az, double el, int wavelength) {
    double u, v, wx, wy, w_elm;
    u = sin(el)*cos(az);
    v = sin(el)*sin(az);
    wx = exp(2*pi*i*(p - 1)*d/wavelength*u);
    wy = exp(2*pi*i*(q - 1)*d/wavelength*v);
    w_elm = wx*wy;
}