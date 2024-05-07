namespace VigenereCipher;
class Program
{
    private static Random random = new Random();

    static void Main(string[] args)
    {
        const string path = @"F:\C#\CipherVisionera\CipherVisionera\CipherConfig.txt";
        const string textPath = @"F:\C#\CipherVisionera\CipherVisionera\Text.txt";

        ReadFromFile(path, textPath, out string plainText, out string key, out string alphabet);
        key = GenerateRandomString(alphabet, plainText.Length);


        VigenereCipher vgc = new VigenereCipher(alphabet, key);

        Console.WriteLine("Alphabet\nKey\tValue\n");

        foreach (var kvp in vgc.alphabet)
        {
            Console.WriteLine($"{kvp.Key}\t{kvp.Value}");
        }

        Console.WriteLine($"\nSize of alphabet: {vgc.alphabet.Count}");

        Console.WriteLine($"Input text: {plainText}\nKey: {key}\n");

        string encryptedText = vgc.Encrypt(plainText);
        Console.WriteLine($"Encrypted Text: {encryptedText}");

        string decryptedText = vgc.Decrypt(encryptedText);
        Console.WriteLine($"Decrypted Text: {decryptedText}");
    }

    public static string GenerateRandomString(string alphabet, int length)
    {
        return new string(Enumerable.Repeat(alphabet, length)
          .Select(s => s[random.Next(s.Length)]).ToArray());
    }

    public static void ReadFromFile(string path, string textPath, out string value,
        out string key, out string alphabet)
    {
        if (!File.Exists(path) || !File.Exists(textPath))
        {
            throw new FileNotFoundException("File wasn`t found");
        }

        value = File.ReadAllText(textPath);

        using (StreamReader file = new StreamReader(path))
        {
            string? line = file.ReadLine().Trim();

            if (line != null) key = line;
            else throw new Exception("Bad config format");

            line = file.ReadLine().Trim();

            if (line != null) alphabet = line;
            else throw new Exception("Bad config format");
        }
    }


}
