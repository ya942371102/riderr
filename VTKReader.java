import java.util.Scanner;
import java.awt.geom.Point2D;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;


public class VTKReader {

  public ArrayList<Point2D> coord = new ArrayList<Point2D>();
  public ArrayList<TriangleFace> tri = new ArrayList<TriangleFace>();
  public ArrayList<Double> field = new ArrayList<Double>();
    
    
  public static void main(String[] args) {
    VTKReader read = new VTKReader();
    String vtkfilename = "riderr.vtk";
    read.readFromFile(vtkfilename);
	    
    System.out.println(read.coord.size());
  }

	
  public void readFromFile(String fname) {
    try {
      BufferedReader bf = new BufferedReader(new FileReader(fname));

      String line;
      line = bf.readLine();

      String start = "DATASET UNSTRUCTURED_GRID";
      while (!line.equals(start)) {
        line = bf.readLine();
      }
		      
      // POINTS num type
      line = bf.readLine();
      Scanner sc = new Scanner(line);
      String tmp = sc.next();
      if (!tmp.equals("POINTS")) {
        System.out.println("Should be: POINTS num type");
      }
		      
      int num_vert;
      num_vert = sc.nextInt();
      sc.close();
		         
      for (int i=0; i<num_vert; ++i) {
        line = bf.readLine();
        sc = new Scanner(line);
        double x = sc.nextDouble();
        double y = sc.nextDouble();
        double z = sc.nextDouble(); // will be 0.0
        if (z != 0.0) {
          System.out.println("z should be 0.0");
        }
		    	  
        Point2D.Double p = new Point2D.Double(x,y);
        coord.add(p);
		    	  
        sc.close();
      }
		      
		      
      line = bf.readLine();
      while(!line.contains("CELLS")) {
        line = bf.readLine();
      }
		      
      // CELLS num1 num2
      sc = new Scanner(line);
      tmp = sc.next();
      int num_tri = sc.nextInt();
      sc.close();
		      
      for (int i=0; i<num_tri; ++i) {
        line = bf.readLine();
        sc = new Scanner(line);
        int v = sc.nextInt();
        if (v != 3) {
          System.out.println("Should be 3 vertices per face");
        }
        int v1 = sc.nextInt();
        int v2 = sc.nextInt();
        int v3 = sc.nextInt();
		    	  
        tri.add(new TriangleFace(v1, v2, v3));
        sc.close();
      }
		      
		      
      line = bf.readLine();
      while(!line.contains("CELL_TYPES")) {
        line = bf.readLine();
      }

      // CELL_TYPES num
      sc = new Scanner(line);
      tmp = sc.next();
      int num_tri2 = sc.nextInt();
      if (num_tri2 != num_tri) {
        System.out.println("Error while reading: CELL_TYPES num");
      }
      sc.close();
		      
      for (int i=0; i<num_tri; ++i) {
        line = bf.readLine();
        sc = new Scanner(line);
        int v = sc.nextInt();
        if (v != 5) {
          System.out.println("Simplex should be a triangle");
        }
        sc.close();
      }
		      
      line = bf.readLine();
      while(!line.contains("POINT_DATA")) {
        line = bf.readLine();
      }
		      
      // POINT_DATA num
      sc = new Scanner(line);
      tmp = sc.next();
      int num_data = sc.nextInt();
      if (num_data != num_vert) {
        System.out.println("Should be as many vertex as scalar values");
      }
		      
      line = bf.readLine(); //SCALARS field double
      line = bf.readLine(); //LOOKUP_TABLE default
		      
      // Read scalar values
      for (int i=0; i<num_data; ++i) {
        line = bf.readLine();
        sc = new Scanner(line);
        double val = sc.nextDouble();
        field.add(val);
      }
		      		      
      bf.close();
      sc.close();
		      
    } catch (IOException e) {
      System.err.println(e);
    }
  }

}
