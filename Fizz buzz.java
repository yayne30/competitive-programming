class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> answer=new ArrayList<String>();
	for(int i=1; i<=n;i++) {
		if (i%3==0&&i%5==0)
			answer.add("FizzBuzz");
		else if(i%3==0)
			answer.add("Fizz");
		else if (i%5==0)
			answer.add("Buzz");
		else
		  answer.add(String.valueOf(i));	
	}
	return answer;
    }
       public static void main(String[] args) {
	Solution mm= new Solution();
	 System.out.println( mm.fizzBuzz(3));
           
        
    }
}
