class Solution {
    public String largestNumber(int[] nums) {
        ArrayList<String[]> list= new ArrayList<>();
        String sresult;
        String[] strArray = Arrays.stream(nums)
                .mapToObj(String::valueOf)
                .toArray(String[]::new);
            list.add(strArray);
        StringBuilder result= new StringBuilder();
       Arrays.sort(strArray, new Comparator<String>() {
           public int compare(String o1, String o2) {
               String s1=o1+o2;
               String s2=o2+o1;
               return s1.compareTo(s2);
           }
       });
      for(int j=strArray.length-1;j>=0;j--){
          if(strArray[strArray.length-1].charAt(0)=='0'){
              result.append(0);
              j=-1; }
           else{
               result.append(strArray[j]);}

       }
       sresult=String.valueOf(result);
       return sresult;



         
    }
}