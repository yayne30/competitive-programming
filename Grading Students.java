
    public static List<Integer> gradingStudents(List<Integer> grades) {
  
                      for(int i=0;i<grades.size();i++){
                           int x=grades.get(i)%5;
                           boolean y= grades.get(i)>=38;
                                if (x>2&&y)
                                 grades.set(i,grades.get(i)+ (5-x));}
                    return grades;
                 }

    }
