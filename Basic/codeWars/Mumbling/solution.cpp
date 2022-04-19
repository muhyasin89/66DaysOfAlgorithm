std::string accum(const std::string &s)
{
    std::string result;

    for (std::size_t i = 0; i < s.size(); ++i)
    {
        if (i) result.push_back('-');

        result.append(1, s[i] &~ 0x20);
        result.append(i, s[i] |  0x20); 
    }   

    return result;
}