package first;

import java.util.Scanner;

public class OnlyNumberOut {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("입력하세요:");
        String str = sc.nextLine();
        Main T=new Main();
        System.out.println(T.solution(str));
    }

    public static class Main {
        public String solution(String str) {
            
            str=str.replaceAll("[^0-9]","");
             
            /*여기까지는 숫자열로만 만들음 하지만
            00125 처럼 앞의 숫자가 0이거나 0의 연속이면 자연수로 만들수가 없음 그래서
            00처럼 앞의 0들을 없애줘야함*/
            str=str.replaceFirst("^0+",""); // 대괄호 밖에 있는(혹은 없는) ^는 시작을 의미하고 +는 뒤의 0이 여러 개있는 경우 모두를 얘기함
            
            /* 2번째 방법!!
            String ans="";
            for(char x:str.toCharArray()) {
                if(Character.isDigit(x)) { //x가 숫자인지 구하는 방법
                    ans+=x;
                    return Integer.parseInt(ans); //뒤에다가 둘것
                    //0280과 같은경우 280으로 변환해줌
             
             !!3번째 방법
             함수를 int형으로 만들고 아스키 번호
             if(x>=48 &&x<=57) ans=ans*10+(x-48)
             x-48을 하는 이유=>0의 아스키 문자가 48이므로 x가 0이면 저걸 해줘야지 원래대로 계산 가능
              */
                
                }
            }
}
