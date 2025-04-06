package dataStructure.school;

import java.util.Scanner;

public class Calculate {
    Scanner sc = new Scanner(System.in);
    int[] arr1;
    int[] arr2;
    String str1="";
    String str2="";

    int[] makeArr(){
        System.out.print("몇차식으로 만들건지 입력하세요:");
        int n = sc.nextInt();
        return new int[n+1];//ex) 2차식이면 x^2+x+c
    }

    void putArr(){
        arr1=makeArr();
        System.out.print("숫자를 입력하세요:");
        for(int i=0;i<arr1.length;i++){
            arr1[i]=sc.nextInt();
        }
        str1=printPoly(arr1);
        System.out.println("식은:"+str1);

        arr2=makeArr();
        System.out.print("숫자를 입력하세요: ");
        for(int i=0;i<arr2.length;i++){
            arr2[i]=sc.nextInt();
        }
        str2=printPoly(arr2);
        System.out.println("식은"+str2);
    }
    String printPoly(int []arr){
        String tmp="";
        for(int i=0;i<arr.length;i++){
            int k=(arr.length-1)-i;
            if(k==0){
                tmp+=arr[i];
            }else {
                tmp += arr[i] + "x^" + k + "+";
            }
        }
        return tmp;
    }


    void printCalculate(){
        System.out.print("계산하고 싶은 연산자를 선택하세요 ex)+,-,* :");
        char c=sc.next().charAt(0);

        switch (c) {
            case '+':
                plusCalculate();
                break;

            case '-':
                minusCalculate();
                break;

            case '*':
                multiplyCalculate();
                break;

            default:
                System.out.println("맞지않은 연산자입니다");
                break;
        }
    }

    int[] returnBig(){
        if(arr1.length>arr2.length){
            return arr1;
        }else return arr2;
    }

    void plusCalculate(){
        int[] sumArr=new int[returnBig().length];
        int maxLen= returnBig().length;

        int gap1=maxLen-arr1.length;
        for(int i=0;i<sumArr.length;i++){
            sumArr[i+gap1]+=arr1[i];
        }

        int gap2=maxLen-arr2.length;
        for(int i=0;i<sumArr.length;i++){
            sumArr[i+gap2]+=arr2[i];
        }

        printPoly(sumArr);


    }

    void minusCalculate(){

        int[] minusArr=new int[returnBig().length];
        int maxLen= returnBig().length;
        /*if(arr1.length>arr2.length){
            minusArr=new int[arr1.length];
        }else{
            minusArr=new int[arr2.length];
        }*/
    }


    void multiplyCalculate(){

    }


    void my_main(){
        putArr(); //2개의 식을 만들음 (각각 수만 들어가있음)
        printCalculate();
    }
    public static void main(String[] args) {
        Calculate cal = new Calculate();
        cal.my_main();
    }
}
