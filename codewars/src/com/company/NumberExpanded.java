package com.company;

public class NumberExpanded {
    public static String expandedForm(int num) {
        StringBuilder expanded = new StringBuilder();
        int length = String.valueOf(num).length();
        String number = String.valueOf(num);
        int localVal=((10*10)*length)/length;
        for (int i=0; i<length; i++){
            //localVal*=length-1;
            if (i==length-1){
                expanded.append(Character.getNumericValue(number.charAt(i))*localVal);
            } else {
                expanded.append(Character.getNumericValue(number.charAt(i))*localVal + "+");
            }
            localVal/=10;
        }

        System.out.println("expanded list: "+ expanded.toString());
        return expanded.toString();
    }

}

