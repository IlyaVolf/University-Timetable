package entities;

public class Auditory {
    public String typesOfClass; // List<String>
    public String capacity; // int
    public String number; // int
    //String description;

    public Auditory(String typesOfClass, String capacity, String number) {
        this.typesOfClass = typesOfClass;
        this.capacity = capacity;
        this.number = number;
    }
}
