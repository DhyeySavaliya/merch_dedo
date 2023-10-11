//Name: Dhyey Savaliya
//Roll No: 202051065
import java.rmi.*;

public class ClientRequest{
    public static void main(String args[]){
        String answer, value = "Reflection in Java";
        try{
            Search access = (Search) Naming.lookup("rmi://localhost:1099/search");
            answer = access.query(value);
            System.out.println("This is  " + value + " " + answer + " at Server of 202051065");
        } 
        catch(Exception ae){
            ae.printStackTrace();
        }
    }
}