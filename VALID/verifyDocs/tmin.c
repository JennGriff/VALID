/**
* @file: 	tmin.c
* @author:	Jennifer Griffiths
*			jjohnson165@mail.csuchico.edu
*
* @section: A program to perform numberical integration using the Trapezoidal Method.  
*/

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

/********************************************************************************
*  FUNCTIONS 
*********************************************************************************/

/** 
 * wolfram
 * A function to calculate 
 *
 * @param   x   the value on which to calculate Wolfram Alpha
 * @return  the results of the calculation
 */
long double wolfram(long double x) {
    return ( (-6)*cosl(x/9) + sqrtl( powl( ((5*sinl(x/3)) + (8*sinl(x/2))) , 4)) + 10 );
}

/** 
 * Trap
 * A function to find the area under the a curve, within bounds
 * 
 * @param   a   left bound
 * @param   b   right bound
 * @param   n   number of trapezoids
 * @return  the estimated area of the trapezoid inder the curve
 */
long double Trap(double a, double b, long double n) {
    long double temp, h, approx;
    int i;

    h = (b - a)/n;
    approx = ((wolfram(a) + wolfram(b)) / 2 );

    for(i=0; i<n; i++){
        temp = a + i*h;
        approx += wolfram(temp);
    }

    approx = h*approx;
    return approx; 
}

/** 
 * ARTE
 * A funtion to calculate the Absolute Relative True Error
 * 
 * @param   tError  true error
 * @param   tValue  true value
 * @return  the absolute relative true error
 */
long double ARTE(long double tError, long double tValue) {
     return fabs(tError / tValue);
}

/** 
 * printReport
 * A function to print the integration result for a given 
 * number of trapezoids and the related ARTE
 *
 * @param   result  integrstion result
 * @param   ARTE    ARTE for tmin
 * @param   n       number of trapazoids
 */
void printReport(long double result, long double error, long double n){
    printf("%.0Lf Trapazoids\n", n);
    printf("Integration Result: %.13Le\n",result);
    printf("ARTE: %.19Le\n", error);
}
/** 
 * PrintSearch
 * A function to print the final results for search mode
 * 
 * @param   result  integrstion result
 * @param   tmin    discovered tmin
 * @param   ARTE    ARTE for tmin
 */
void printSearch(long double result, long double error, long double tmin){
    printf("***********************************\n");
    printf("tmin: %.19Le\n", tmin);
    printf("Integration Result: %.13Le\n",result);
    printf("ARTE: %.19Le\n", error);
    printf("***********************************\n");
}
/********************************************************************************
*  Main 
*********************************************************************************/

int main() {
    long double trueValue, criteria, a, b, t, arte, tError, trapResult, adder; 
    char flag;
    adder = 1000;
    arte = 1;
    /* hard coded values */
    trueValue = 6745.9948824470072783;
    criteria = 0.5*powl(10, -14);

    scanf("%c %Lf %Lf %Lf",&flag, &a, &b, &t );

    /************************
        SEARCH MODE
    *************************/
    if(flag == 'S') {
        do{
            trapResult = Trap(a, b, t);
            /* calculate ture error */
            tError = trueValue - trapResult;
            arte = ARTE(tError, trueValue);
            printReport(trapResult, arte, t);
            t += adder; 
        } while(arte > criteria);

        printSearch(trapResult, arte, t);
    }

    /************************
        REPORT MODE
    *************************/
    else if(flag == 'R') {
        trapResult = Trap(a, b, t);

        tError = trueValue - trapResult;
        arte = ARTE(tError, trueValue);
        printReport(trapResult, arte, t);
    }
    return 0;
}

