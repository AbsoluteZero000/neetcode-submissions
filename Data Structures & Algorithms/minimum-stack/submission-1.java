class MinStack {
    private Integer currMin;
    private ArrayList<Integer> lst;
    private Integer currTop;
    public MinStack() {
        lst = new ArrayList<>();
        currMin = Integer.MAX_VALUE;
        currTop = 0;
    }
    
    public void push(int val) {
        if(currTop == lst.size()) {lst.add(val);}
        else {lst.set(currTop, val);}
        currTop++;

        if(val < currMin){
            currMin = val;
        }
    }
    
    public void pop() {
        currTop--;
        if(lst.get(currTop).equals(currMin)){
            currMin = findMin();
        }
        
    }
    
    public int top() {
        return lst.get(currTop-1);
        
    }
    
    public int getMin() {
        return currMin;
    }

    private int findMin(){
        int min = Integer.MAX_VALUE;
        for(int i = 0; i < currTop; i++){
            if(min > lst.get(i))
                min = lst.get(i);
        }
        return min;
    }
}
