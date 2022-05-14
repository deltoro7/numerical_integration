def left_end(a,b,f):
    return a


def right_end(a,b,f):
    return b


def midpoint(a,b,f):
    return (a+b) / 2


def simpson(f, a, b, num_ints):
    if num_ints == 1:
        num_ints =2
    h=(b-a)/num_ints
    k=0.0
    x=a + h
    for i in range(1,num_ints/2 + 1):

        k = k+  (4*f(x))
        x = x + (2*h)

    x = a + (2*h)
    for i in range(1,num_ints/2):

        k = k+  (2*f(x))
        x = x + (2*h)
    return n((h/3)*(f(a)+f(b)+k))



#def trap(a,b,f):
  #  return (f(a) + f(b)) / 2


def trapezoid(f,a,b,num_ints):
            h = (b-a) / num_ints
            s = (f(a) + f(b)) #computes first and last
            i = 1
            while i < num_ints:
                s += 2 * f(a + i *h)
                i += 1
            return ((h/ 2 ) * s)



def integral(f, a, b, num_ints, choose_xi):
    if choose_xi == simpson:

        simpson_value = simpson(f,a,b,num_ints)
        return simpson_value


    if choose_xi ==trapezoid:
        trap_value = trapezoid(f,a,b,num_ints)
        return trap_value

    else: #works for midpoint/ right end
        h = (b-a) / num_ints                                #width of subinterval
        total = 0
        for i in range(num_ints):
            subinterval_start = a + (i*h)
            subinterval_end = subinterval_start + h

            xi = choose_xi(subinterval_start, subinterval_end,f)

            total = total + ( f(xi) * h )


        return n(total)


def percent_error(estimate, actual):
    percent = abs(estimate- actual) / actual
    return percent



Integral_Table_Tolerance = 0.0000000001
def generate_integral_table(f , a , b, choose_xi, correct=None):
   # estimate = None
    previous_error = 0
    for r in range(6):
        num_ints = 10**r

        estimate = integral(f, a, b , num_ints, choose_xi) #computes the actual integral
        first_error  = percent_error(estimate,correct)


        #output =  "Number_intervals = ", num_ints, "integral estimate = ", estimate


        print("\n")
        #error calc
        new_error = first_error
        output =  "Number_intervals = ", num_ints, "integral estimate = ", estimate, "error change % = ", (new_error-previous_error)*100
        print(output)

        previous_error = new_error

        #code to produce the realative change



###code to execute
#import math
#def f(x):
    return (x)**0.5
#correct_value = 666

#print("midpoint")

#generate_integral_table(f,1,100, choose_xi = midpoint, correct = correct_value)


#print("\n")
#print("now trap")

#generate_integral_table(f,1,100, choose_xi = trapezoid, correct = correct_value)

#print("\n")
#print("now simpson")
#generate_integral_table(f,1,100, choose_xi = simpson, correct =correct_value)                
