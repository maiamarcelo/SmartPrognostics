/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package smartprognostics;

/**
 *
 * @author MarcelodeAlmeidaMaia
 */
public class Config {
    private String modelFile = "";
    private String patientFile = "";
    private String resultFile;
    private boolean resultSaved = true;
    
    public boolean isResultSaved () {
        return resultSaved;
    }
    
    public String getModelFile () {
        return modelFile;
    }
    
    public String getPatientFile () {
        return patientFile;
    }
    
    public String getResultFile () {
        return resultFile;
    }
    
    public void setModelFile (String f) {
        modelFile = f;
    }
    
    public void setPatientFile (String f) {
        patientFile = f;
    }
    
    public void setResultFile (String f) {
        resultFile = f;
    }
    
}
