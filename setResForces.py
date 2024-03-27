import sys
import subprocess

def main(argv):
    # inputs
    args = argv[-7:]

    tempFolder = args[0]
    stepName = args[1]
    modelName = args[2]
    IGLnodesSetName = args[3]
    instanceName = args[4]
    send = args[5]
    suppress = args[6]

    pyFile = tempFolder + "\\Abaqus_setForces"
    modelPath = tempFolder + "\\GlobalModel.cae"
    aux = "noGUI="+pyFile

    cmd = ["C:\\SIMULIA\\Commands\\abaqus.bat", "cae", aux, "--", modelPath, stepName, modelName, IGLnodesSetName, instanceName, send, suppress]
    subprocess.call(cmd)

if __name__=="__main__":
    main(sys.argv)