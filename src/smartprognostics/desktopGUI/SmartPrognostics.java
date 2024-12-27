/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package smartprognostics.desktopGUI;
/**
 *
 * @author MarcelodeAlmeidaMaia
 */
import smartprognostics.desktopGUI.MainJFrame;
import javax.swing.JFrame;
import java.awt.Dimension;
import java.awt.Toolkit;
public class SmartPrognostics {

/**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        sleepThread();
       
         java.awt.EventQueue.invokeLater(new Runnable() {

            @Override
            public void run() {
                Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
                JFrame mainFrame = new MainJFrame();
                mainFrame.setBounds(0,0,(int)(screenSize.width/1.2), (int)(screenSize.height/1.2));
                mainFrame.setVisible(true);
                mainFrame.setTitle("Smart Prognostics");
                mainFrame.toFront();
    
            }
        });
    }
   
     private static void sleepThread() {
        try
            {
                Thread.sleep(3000);
            }
            catch (InterruptedException ex)
            {
                // Do something, if there is a exception
                System.out.println(ex.toString());
            }
    }
    
}
