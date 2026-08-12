//method over loading example with add method
class methodoverloadingex
{
void add(int a,int b) 
{
System.out.println("addition of a A and B:" +(a+b));
}
void add(int a,int b,int c) 
{
System.out.println("addition of a A ,B and C:" +(a+b));
}
void add(double a,double b) 
{
System.out.println("addition of a A and B:" +(a+b));
}
void add(double a,double b,double c) 
{
System.out.println("addition of a A,B and C:" +(a+b));
}
public static void main(String[] args){
    methodoverloadingex obj=new methodoverloadingex();
    obj.add (2,4);
    obj.add(2,4,6);
    obj.add(1.5,0.5);
    obj.add(1.2,1.4,1.5);
}

}