def extract_metrics(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    wer = []; cer = []; loss = []
    for line in lines:
        if line.find("Average Loss") > 0:
            loss.append(float(line.strip().split(" ")[-1]))
        if line.find("Average WER") > 0:
            line = line.strip().split("\t")
            wer.append(float(line[-2].split(" ")[-1])); cer.append(float(line[-1].split(" ")[-1]))
    return loss, wer, cer
