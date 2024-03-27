import sys
import subprocess
import shutil

def main(argv):
    # inputs
    args = argv[-5:]

    jobFolder = args[0]
    tempFolder = args[1]
    stepName = args[2]
    jobName = args[3]
    cpus = int(args[4])

    pyFile = tempFolder + "\\Abaqus_run"
    modelPath = tempFolder + "\\GlobalModel.cae"
    aux = "noGUI="+pyFile
    cmd = ["C:\\SIMULIA\\Commands\\abaqus.bat", "cae", aux, "--", modelPath, jobName, str(cpus)]
    subprocess.call(cmd)

    
    shutil.copy(jobFolder + "\\" + jobName + ".odb", tempFolder + "\\" + jobName + ".odb")

    # writing element forces on file
    obdFile = tempFolder + "\\" + jobName + ".odb"
    pyFile = tempFolder + "\\Abaqus_getElementNodalForces"
    aux = "noGUI="+pyFile
    cmd = ["C:\\SIMULIA\\Commands\\abaqus.bat", "cae", aux,"--", obdFile, stepName]
    subprocess.call(cmd)

    pyFile = tempFolder + "\\Abaqus_getDisplacements"
    aux = "noGUI="+pyFile
    cmd = ["C:\\SIMULIA\\Commands\\abaqus.bat", "cae", aux, "--", obdFile, stepName]
    subprocess.call(cmd)

    shutil.copy(jobFolder + "\\" + "forcesAbaqus.txt", tempFolder + "\\forcesAbaqus.txt")
    shutil.copy(jobFolder + "\\" + "displacementsAbaqus.txt", tempFolder + "\\displacementsAbaqus.txt")   


if __name__=="__main__":
    main(sys.argv)