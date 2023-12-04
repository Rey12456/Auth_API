import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class JUnitTest {

    // Test to check the size of the list after adding and removing elements
    @Test
    void testSizeofList() {
        MyList<Integer> list = new MyList<>();
        assertTrue(list.size()==0); // Ensure the initial size is 0

        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);

        assertFalse(list.size()!=4); // Ensure the size is now 4

        list.remove(0);
        list.remove(1);

        assertFalse(list.size()!=2); // Ensure the size is 2 after removals

        }


    // Test to add 100 numbers to the list and check if they are in ascending order
    @Test
    void add100Numbers() {
        MyList<Integer> list = new MyList<>();

        for (int i = 0; i < 100; i++) {
            list.add(i + 1);

        }
        for (int i = 0; i < 100 - 1; i++) {
            assertTrue(list.get(i) < list.get(i + 1)); // Check if elements are in ascending order
        }
    }

    // Test case to remove elements from the ends of the list. (From the first and last index)
    @Test
    void removingFromEnds() {

        MyList<String> list = new MyList<>();
        list.add("apple");
        list.add("banana");
        list.add("cherry");
        list.add("durian");

        // Removes the last element and check if the previous to last element is now at the end
        String threeWas = list.remove(list.size() - 1);
        String twoIs = list.get(list.size() - 1);

        assertTrue((threeWas.equals("durian") && twoIs.equals("cherry")));

        // Removes the first element and check if the previous to second element is now at the beginning
        String zeroWas = list.remove(0);
        String zeroIs = list.get(0);

        assertTrue((zeroWas.equals("apple") && zeroIs.equals("banana")));


    }


}