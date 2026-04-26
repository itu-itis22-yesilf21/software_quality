import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sortNumbers("three one five")
    "one three five"
     */
    public String sortNumbers(String numbers) {
        String[] nums = numbers.split(" ");
        List<Integer> num = new ArrayList<>();
        for (String string : nums) {
            switch (string) {
                case "zero":
                    num.add(0);
                    break;
                case "one":
                    num.add(1);
                    break;
                case "two":
                    num.add(2);
                    break;
                case "three":
                    num.add(3);
                    break;
                case "four":
                    num.add(4);
                    break;
                case "five":
                    num.add(5);
                    break;
                case "six":
                    num.add(6);
                    break;
                case "seven":
                    num.add(7);
                    break;
                case "eight":
                    num.add(8);
                    break;
                case "nine":
                    num.add(9);
                    break;
                default:
                    break;
            }
        }
        Collections.sort(num);
        List<String> result = new ArrayList<>();
        for (int m : num) {
            switch (m) {
                case 0:
                    result.add("zero");
                    break;
                case 1:
                    result.add("one");
                    break;
                case 2:
                    result.add("two");
                    break;
                case 3:
                    result.add("three");
                    break;
                case 4:
                    result.add("four");
                    break;
                case 5:
                    result.add("five");
                    break;
                case 6:
                    result.add("six");
                    break;
                case 7:
                    result.add("seven");
                    break;
                case 8:
                    result.add("eight");
                    break;
                case 9:
                    result.add("nine");
                    break;
                default:
                    break;
            }
        }
        return String.join(" ", result);
    }
}
