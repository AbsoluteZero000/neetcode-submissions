class Solution {
    public boolean isValid(String s) {
        ArrayList<Character> stk = new ArrayList<>();
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[')
                stk.add(s.charAt(i));
            else{
                if( stk.size() > 0 &&
                    (
                        (s.charAt(i) == ')' && stk.get(stk.size() - 1) == '(') || 
                        (s.charAt(i) == '}' && stk.get(stk.size() - 1) == '{') || 
                        (s.charAt(i) == ']' && stk.get(stk.size() - 1) == '[') 
                    )
                ){
                    stk.remove(stk.size()-1);
                } else return false;
            }
        } 
        return stk.size() == 0;
    }
}
