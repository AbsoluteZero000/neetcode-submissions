class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> lst = new HashMap<>();
        for(String str: strs){
            String s= str.chars().boxed().sorted().map(Character::toString).sorted().collect(Collectors.joining())
        .toString();
            if(lst.containsKey(s)){
                lst.get(s).add(str);
            } else {
                lst.put(s, new ArrayList<String>(List.of(str)));
            }
        }
        return  new ArrayList<>(lst.values());

        
    }
}
