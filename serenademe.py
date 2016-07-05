import os
def main():
  #purposefully hardcoded text path for ease of use trying to switch to web based api for lyrics
  with open("lyrics.txt", "r") as f:
     for line in f:
        sing = "say " + str(line)
        os.system(sing)
        
if __name__ == '__main__':
  main()
