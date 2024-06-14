#StringBuilder()를쓰면 여러가지 함수를 쓸수있음 ex)reverse
import java.util.ArrayList;
import java.util.Scanner;

public class ReverseWord {
    public static void main(String[] args) {
        Main T=new Main();
        Scanner sc = new Scanner(System.in);
        int num=sc.nextInt();


        String[] str=new String[num];
        for(int i=0;i<num;i++){
            str[i]=sc.next();

        }
        for(String x:T.solution(num,str)){
            System.out.println(x);
        }
    }

    public static class Main {
        public ArrayList<String> solution(int n,String[] str){
            ArrayList<String> answer=new ArrayList<>();
            for(String x:str){
                String tmp=new StringBuilder(x).reverse().toString();
            //StringBuilder이라는 객체 내부의 reverse()함수를 쓰고 다시 String으로 바꾸기위해 toString
                 answer.add(tmp);
                 //arraylist에 추가하는건 add
            }
            return answer;

        }
        /*public String solution(String str1) {
            char[] ans = str1.toCharArray();
            // String []ans=new String[str1.length()];
            // str1.toCharArray();
            //String realans=" ";
            for (int i = 0; i < str1.length() / 2; i++) {

                char tmd = ans[i];
                ans[i] = ans[str1.length() - i - 1];
                ans[str1.length() - i - 1] = tmd;

            }


            return new String(ans);
        }*/

    }
}
