namespace VigenereCipher;

public class VigenereCipher
{
    public Dictionary<char, int> alphabet { get; private set; }
    private Dictionary<int, char> _alphabetReversed;
    public string key { get; private set; }

    public VigenereCipher(string alphabet, string key)
    {
        char[] sortedAlphabet;
        char[] uniqueKeyLetters = key.Distinct().ToArray();

        if (uniqueKeyLetters.Length == 0)
        {
            throw new Exception("Bad provided key.");
        }

        foreach (char letter in uniqueKeyLetters)
        {
            if (!alphabet.Contains(letter))
            {
                throw new Exception("Alphabet is not matched to provided key.");
            }
        }

        this.alphabet = new Dictionary<char, int>();
        this.key = key;

        sortedAlphabet = alphabet.Trim().Distinct().ToArray();
        Array.Sort(sortedAlphabet);

        for (int i = 0; i < sortedAlphabet.Length; ++i)
        {
            this.alphabet.Add(sortedAlphabet[i], i);
        }

        _alphabetReversed = ReverseDictionary(this.alphabet);
    }

    public string Encrypt(string value)
    {
        char[] encryptLetters;
        int keyCounter = 0, moduleSum = 0;

        if (value.Length == 0)
        {
            return "";
        }

        encryptLetters = new char[value.Length];

        for (int i = 0; i < value.Length; ++i)
        {
            if (keyCounter == key.Length)
            {
                keyCounter = 0;
            }

            moduleSum = this.alphabet[value[i]] + this.alphabet[key[keyCounter]];

            if (moduleSum >= alphabet.Count)
            {
                moduleSum -= alphabet.Count;
            }

            encryptLetters[i] = _alphabetReversed[moduleSum];

            ++keyCounter;
        }

        return new string(encryptLetters);
    }

    public string Decrypt(string value)
    {
        char[] decryptLetters;
        int keyCounter = 0, moduleSubtraction = 0;

        if (value.Length == 0)
        {
            return "";
        }

        decryptLetters = new char[value.Length];

        for (int i = 0; i < value.Length; ++i)
        {
            if (keyCounter == key.Length)
            {
                keyCounter = 0;
            }

            moduleSubtraction = this.alphabet[value[i]] - this.alphabet[key[keyCounter]];

            if (moduleSubtraction < 0)
            {
                moduleSubtraction += this.alphabet.Count;
            }

            decryptLetters[i] = _alphabetReversed[moduleSubtraction];

            ++keyCounter;
        }

        return new string(decryptLetters);

    }

    private Dictionary<int, char> ReverseDictionary(Dictionary<char,int> originalDict)
    {
        Dictionary<int, char> reverseDict = new Dictionary<int, char>();

        foreach (var kvp in originalDict)
            reverseDict.Add(kvp.Value, kvp.Key);

        return reverseDict;
    }
}
