class Solution {

    public String encode(List<String> strs) {
        String res = "";
        for(String str: strs){
            res += Integer.toString(str.length()) + '#' + str;
        }
        System.out.println(res);
        return res;
    }

    public List<String> decode(String str) {
        ArrayList<String> res = new ArrayList<>();
        Integer i = 0;
        while(i < str.length()){
            String currSize = "";
            while(str.charAt(i) != '#'){
                currSize += str.charAt(i);
                i++;
            }
            i++;

            System.out.println(currSize + ";");
            Integer actualSize = Integer.parseInt(currSize);
            Integer begin = i;
            String word = "";

            while(i < begin + actualSize){
               word += str.charAt(i);
               i++; 
            }

            res.add(word);
        }
        return res;
    }
}
