#define TRUE 1

class AntElm {
    public:
        int row;
        int col;
        WaveVector w;
        bool lock;      /* indicates if array element is in use */

	/*  
	    Calculates phase offset applied to antenna element (p,q) === (row,col) given 
	    a transmit direction or DoA in spherical coordinates (az,el) === (φ,θ) 
	    and the signal wavelength λ.
	    Actual phase offset is given by ψ = (-2*π*(p-1)*d/λ)*u
	    E-field contribution is given by taking exp(i*ψ).
	*/
        void setPhase(int row, int col, double az, double el, int wavelength) {
	    double u, v, wx, wy, s_phase;
	    u = sin(el)*cos(az);
       	    v = sin(el)*sin(az);
	    wx = -2*pi*i*(row - 1)*d/wavelength*u;
	    wy = -2*pi*i*(col - 1)*d/wavelength*v;
	    (*this).w.phase_offset = wx + wy;                  /* Steering phase */
        }

	void addPhase() {
	
	}
};

/*
    arrayFactor() might be superfluous for transmit applications but
    may be needed for DoA application.
    Potential approach:

    1) Calculate cross correlation of all elements with respect to a
    reference signal to obtain phase differences for all antenna 
    elements with respect to the reference signal.

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
