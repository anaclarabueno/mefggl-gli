import sys
import subprocess

def main(argv):
    # inputs
    args = argv[-6:]

    tempFolder = args[0]
    stepName = args[1]
    modelName = args[2]
    instanceName = args[3]
    dispFile = args[4]
    suppress = args[5]

    pyFile = tempFolder + "\\Abaqus_setDisplacements"
    modelPath = tempFolder + "\\GlobalModel.cae"
    aux = "noGUI="+pyFile
    cmd = ["C:\\SIMULIA\\Commands\\abaqus.bat", "cae", aux, "--", modelPath, stepName, modelName, instanceName, dispFile, str(int(suppress))]
    subprocess.call(cmd)

if __name__=="__main__":
    main(sys.argv)