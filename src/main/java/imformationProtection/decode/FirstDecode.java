package imformationProtection.decode;


import java.util.*;

public  class FirstDecode {
    Scanner sc=new Scanner(System.in);
    String str=sc.nextLine();
        HashMap<Character,Integer> map=new HashMap<>();
    char[] chr = str.toCharArray();

    void putFrequency(){
        for(char c : chr) {
            if (c >= 65 && c <= 90) {
                map.put(c, map.getOrDefault(c, 0) + 1);
            }
        }

        sortingWithValues();
    }

    void sortingWithValues(){ // comparator사용
        List<Character> keyList=new ArrayList<>();
        for(Character chr:map.keySet()){
            keyList.add(chr);  //키 리스트에 키값 대입
        }
        keyList.sort(new Comparator<Character>() {

            @Override
            public int compare(Character o1, Character o2) {
                return map.get(o2).compareTo(map.get(o1)); // 내림차순 정리를 위한 Comparator
            }
        });
        for(Character chr:keyList){
            System.out.print(chr+":"+map.get(chr)+" ");
        }
        System.out.println();

        //젤 많은 3가지 많은것 (P:156 ,H:124 ,S:116)  =>t h e 일 가능성이 높음  총경우 3!
    }
    void decryption(){
       String dstr= str
                .replace('P','e')
                .replace('S','t')
                .replace('O','h') //1

                .replace('K','i')
                .replace('H','a') //2

                .replace('M', 'o') //3

                .replace('V','m')
                .replace('X','r')
                .replace('T','w')


                .replace('A','l')

                .replace('D','g')
                .replace('B','n')
                .replace('U','s')
                .replace('E','c')
                .replace('L','d')
                .replace('J','y')
                .replace('Z','u')
                .replace('Q','f')
                .replace('W','p')

                .replace('C','v')
                .replace('G','q')
                .replace('I','b')
                .replace('F','j')
                .replace('R','k');


 /*1.SOP가 중복 SOP==THE라고 생각 ,
   2.단독 문자 K, H 가 I OR A  =>변동 가능
   3. TM이 단독으로 나옴 ->TO라 생각
   4.SMVMXXMT->TOVOXXOT=>안바뀐것은 V,X,T =>예상 TOMORROW  => V->M ,X->R , T->W
   5.waAAow ->wallow
   6.toDether ->together
   7.meaBiBg->meaning
   8.Uee->see
   9.ameriEan->american
   10.chilLren->children
   11.todaJ->today
   12.yoZ,oZt, trZe-> Z->u
   13.Qriends->friends
   14. desWair->despair ,uW->up
   15.eCen->even
   16.eGual->equal
   17.Ie,Irotherhood ->I==b
   18.Fudged ,Fustice ->F==j
   19.blacR=>black
  */
        System.out.println(dstr);
    }


    public void myMain(){
        putFrequency(); //빈도수 확인용
        decryption();
    }


    public static void main(String[] args) {
        FirstDecode f=new FirstDecode();
        f.myMain();
    }
}





