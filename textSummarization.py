from reader import csvReader
import train
import test

def main():
    train = True
    fileDir = "data/news_summary.csv"
    data = csvReader.getData(fileDir)

    if train:
        """Train Data"""

    else:
        """Train Data"""



if __name__ == "__main__":
    main()