
import java.util.Map;
import java.util.HashMap;

public class MyClass {
    private Map<String, Integer> map;

    public MyClass() {
       map = new HashMap<>();
       map.put("foo", 1);
       map.put("bar", 3);
    }

    public Integer getValue(String input, int numRetries) {
       try {
          return map.get(input);
       } catch (Exception e) {
          if (numRetries > 3) {
             throw e;
          }
          return getValue(input, numRetries + 1);
       }
    }
}

