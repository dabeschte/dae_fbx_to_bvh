import os

in_path = "D:/Seafile/Eva Videos/"
out_path = "D:/nnvrik-tpose-bvh/"

for folder in list(os.walk(in_path))[0][1]:
    for file in list(os.walk(in_path+folder))[0][2]:
        if file.endswith(".bvh"):
            with open(in_path+folder+"/"+file, "r") as f:
                text = ""
                for i in range(127):
                    text += f.readline()
                frames = str(int(f.readline().split("Frames:    ")[1]) + 1)
                text += "Frames: " + frames + "\n"
                text += f.readline()
                text += "0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0\n"
                # for line in f.readlines():
                #     text += line
                text += f.read()
                # print(text)
                if not os.path.exists(out_path + folder):
                    os.makedirs(out_path + folder)
                with open(out_path + folder + "/" + file, 'w+') as out_file:
                    out_file.write(text)
