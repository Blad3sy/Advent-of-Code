using System;
using System.Collections.Generic;
using System.IO;

namespace Program {
    class Program {
        static long[] MapConvert(long[] destNums, long[] sourceNums, long[] counts, long[] seeds) {
            long[] finalSeeds = new long[seeds.Length];
            long dif;

            Array.Copy(seeds, finalSeeds, seeds.Length);

            for (int i = 0; i < counts.Length; i++) {
                dif = destNums[i] - sourceNums[i];
                for (int t = 0; t < seeds.Length; t++) {
                    if (seeds[t] >= sourceNums[i] && seeds[t] < sourceNums[i] + counts[i]) {
                        finalSeeds[t] = seeds[t] + dif;
                    }
                }
            }

            return finalSeeds;
        }
        static void Main (string[] args) {
            string filePath = @"B:\VSCODE Programs\Advent-of-Code-2023\solutions\files\day5input.txt";
            string[] fileLines = File.ReadLines(filePath).ToArray();

            List<List<long>[]> fullPathMap = new List<List<long>[]>();

            List<long[]> seeds = new List<long[]>();
            List<long> subSeeds = new List<long>();
            string numConstructor = "";

            fileLines[0] += " ";
            // This code shouldn't be necessary!

            for (int i = 0; i < fileLines[0].Length; i++) {
                if (Char.IsNumber(fileLines[0][i])) {
                    numConstructor += fileLines[0][i];
                }
                else if (fileLines[0][i] == ' ') {
                    if (numConstructor != "") {
                        subSeeds.Add(Convert.ToInt64(numConstructor));
                        numConstructor = "";
                    }

                    if (subSeeds.Count == 2) {
                        seeds.Add(subSeeds.ToArray());
                        subSeeds.Clear();
                    }
                }
            }

            bool onNumLine = false;
            numConstructor = "";
            List<long> lineNums = new List<long>();
            string currentLine;

            List<long> destNums;
            List<long> sourceNums;
            List<long> counts;

            for (int i = 1; i < fileLines.Length; i++) {
                currentLine = fileLines[i] + " ";

                if (string.IsNullOrWhiteSpace(currentLine)) {
                    if (lineNums.Any()) {
                        destNums = new List<long>();
                        sourceNums = new List<long>();
                        counts = new List<long>();

                        for (int t = 0; t < lineNums.Count; t++) {
                            if (t % 3 == 0) {
                                destNums.Add(lineNums[t]);
                            }
                            if (t % 3 == 1) {
                                sourceNums.Add(lineNums[t]);
                            }
                            if (t % 3 == 2) {
                                counts.Add(lineNums[t]);
                            }
                        }
                        fullPathMap.Add([destNums, sourceNums, counts]);
                    }
                    onNumLine = false;
                    lineNums = new List<long>();
                }

                if (onNumLine) {
                    for (int t = 0; t < currentLine.Length; t++) {
                        if (Char.IsNumber(currentLine[t])) {
                            numConstructor += currentLine[t];
                        }
                        else if (currentLine[t] == ' ') {
                            if (numConstructor != "") {
                                lineNums.Add(Convert.ToInt64(numConstructor));
                                numConstructor = "";
                            }
                        }
                    }
                }

                if (Char.IsLetter(currentLine[0])) {
                    onNumLine = true;
                }
            }

            long lowest = 10000000000;
            List<long> actualSeeds;
            long[] actualSeedsArray;
            int counter;

            foreach (long[] seed in seeds) {
                actualSeeds = new List<long>();

                for (long i = seed[0]; i < seed[0] + seed[1]; i++) {
                    actualSeeds.Add(i);
                }
                Console.WriteLine("LIST CREATION DONE\n");

                actualSeedsArray = actualSeeds.ToArray();
                counter = 1;
                foreach (List<long>[] path in fullPathMap) {
                    actualSeedsArray = MapConvert(path[0].ToArray(), path[1].ToArray(), path[2].ToArray(), actualSeedsArray);
                    Console.WriteLine($"CONVERSION {counter} DONE");
                    counter++;
                }
                Console.WriteLine("\nMAPPING DONE");

                Array.Sort(actualSeedsArray);

                if (actualSeedsArray[0] < lowest) {
                    lowest = actualSeedsArray[0];
                }
            }

            Console.WriteLine(lowest);
        }
    }
}