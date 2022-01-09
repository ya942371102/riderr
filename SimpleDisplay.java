import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.geom.Point2D;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JPanel;


public class SimpleDisplay {

  public static void main(String[] args) {
    JFrame f = new JFrame("Simple");

    int w = 1000;
    int h = 600;
		
    // Read a (2D) triangulation from a vtk
    if (args.length != 1) {
      Usage();
      System.exit(1);
    }
    
    VTKReader read = new VTKReader();
    String vtkfilename = args[0];
    read.readFromFile(vtkfilename);

    ArrayList<Point2D> coord = read.coord;
    ArrayList<TriangleFace> tri = read.tri;
	    
    DrawPanel dp = new DrawPanel(w, h, coord, tri);

    f.add(dp, BorderLayout.CENTER);
    f.pack();
    f.setSize(w, h);
    f.setVisible(true);
		
    f.addWindowListener(new WindowAdapter() {
        public void windowClosing(WindowEvent e) {
          System.exit(0);
        }
      });
  }

  
  private static void Usage() {
    System.out.println("Usage:");
    System.out.println("java SimpleDisplay file.vtk");
    System.out.println("where: file.vtk is a 2D triangulation saved in the VTK file format");
  }
}


class DrawPanel extends JPanel {
  ArrayList<Point> lines = new ArrayList<Point>();

  ArrayList<Point2D> coord;
  ArrayList<Point2D> scaledCoord;
  ArrayList<TriangleFace> tri;
        
  public DrawPanel(int w, int h, ArrayList<Point2D> coord, ArrayList<TriangleFace> tri) {
    setBackground(Color.white);

    this.coord = coord;
    this.tri = tri;
        
    // Need to map window in pixel to bounding box of tri mesh
    Point2D minpt = new Point2D.Double();
    Point2D maxpt = new Point2D.Double();
        
    findBBox(minpt, maxpt);
                
    // Rescale coordinates: (0,0) corresponds to minpt
    // (w, h) corresponds to maxpt
    scaledCoord = new ArrayList<Point2D>();
    rescale(minpt, maxpt, w, h);
  }

  private void rescale(Point2D minpt, Point2D maxpt, int w, int h) {
    int scale_factor = Math.min(w, h);
    
    int num_coord = coord.size();
    double d = Point2D.distance(minpt.getX(), minpt.getY(), maxpt.getX(), maxpt.getY());

    double scaledMaxx = maxpt.getX() - minpt.getX();
    scaledMaxx = scaledMaxx / d;
    	
    double scaledMaxy = maxpt.getY() - minpt.getY();
    scaledMaxy = scaledMaxy / d;
    	
    double centerw = w/2.0;
    double centerh = h/2.0;
    	
    for (int i =0; i<num_coord; ++i) {
      Point2D p = coord.get(i);
      double x = p.getX();
      double y = p.getY();
        		
      x = x - minpt.getX();
      y = y - minpt.getY();
    		
      x = x / d;
      y = y / d;
    	
      x = (scale_factor-1)*x;
      y = (scale_factor-1)*y;
    		
      // At this point in time the mesh is upside down so flip it
      y = -y;
      // and translate it
      y = y + scaledMaxy*(scale_factor-1);
    		
      // may not be centered, so center it
      x = (x-scaledMaxx*(scale_factor-1)/2) + centerw;
      y = (y-scaledMaxy*(scale_factor-1)/2) + centerh;
    		
      Point2D scaledp = new Point2D.Double(x,y);
      scaledCoord.add(scaledp);
    }
  }
    
  private void findBBox(Point2D minpt, Point2D maxpt) {
    minpt.setLocation(1e10, 1e10);
    maxpt.setLocation(-1e10, -1e10);
    	
    int num_vert = coord.size();
    	
    for (int i=0; i<num_vert; ++i) {
      double minx = minpt.getX();
      double miny = minpt.getY();
      double maxx = maxpt.getX();
      double maxy = maxpt.getY();
    		
      Point2D curr = coord.get(i);
    		
      minx = Math.min(minx, curr.getX());
      miny = Math.min(miny, curr.getY());
    		
      maxx = Math.max(maxx, curr.getX());
      maxy = Math.max(maxy, curr.getY());
        	
      minpt.setLocation(minx, miny);
      maxpt.setLocation(maxx, maxy);
    }
  }

  public void paint(Graphics g) {
    int num_tri = tri.size();
        
    g.setColor(Color.black);
    	
    for (int i=0; i<num_tri; ++i) {
      TriangleFace t = tri.get(i);
    		
      int v1 = t.v1;
      int v2 = t.v2;
      int v3 = t.v3;
    		
      int[] xp = new int[3];
      int[] yp = new int[3];
    		
      xp[0] = (int)scaledCoord.get(v1).getX();
      xp[1] = (int)scaledCoord.get(v2).getX();
      xp[2] = (int)scaledCoord.get(v3).getX();

      yp[0] = (int)scaledCoord.get(v1).getY();
      yp[1] = (int)scaledCoord.get(v2).getY();
      yp[2] = (int)scaledCoord.get(v3).getY();

      g.drawPolygon(xp,yp,3);
    }

  }
}

