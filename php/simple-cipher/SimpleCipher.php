<?php

declare(strict_types=1);


class SimpleCipher
{
    const START_CODE_POINT = 97; # the letter 'a'

    public string $key;

    public function __construct(
        string $key = 'aaaaaaaaaa'
    ) {
        if ($key === '') {
            throw new \InvalidArgumentException('empty key forbidden');
        }

        if ($key !== static::normalize($key)) {
            throw new \InvalidArgumentException('must be only ASCII lowercase alpha chars');
        }

        $this->key = $key;
    }

    private static function normalize(string $text): string
    {
        return \strtolower(
            preg_replace(
                '/\PL/u',
                '',
                $text
            )
        );
    }

    private static function charOffset(string $char): int
    {
        return \ord($char) - static::START_CODE_POINT;
    }

    private static function charTransform(
        string $char,
        int $offset
    ): string {
        $alphaPosition = static::charOffset($char);
        $transformedAlphaPosition = ($alphaPosition + $offset) % 26;
        $transformedCodePoint = $transformedAlphaPosition + static::START_CODE_POINT;

        return \chr(
            $transformedCodePoint
        );
    }

    /** @return \Generator<string> */
    private function offsetGenerator(): \Generator
    {
        while (true) {
            foreach (\str_split($this->key) as $char) {
                yield static::charOffset($char);
            }
        }
    }

    private static function offsetStep(\Generator &$generator): int
    {
        /** @var int */
        $value = $generator->current();
        $generator->next();

        return $value;
    }

    /**
     * 
     * @param string $text to cipher
     * @param int $mode 1:encode / -1:decode
     * @return string 
     */
    private function codec(string $text, int $mode = 1): string
    {
        $offsetGenerator = $this->offsetGenerator();

        return \join(
            \array_map(
                fn (string $char): string => static::charTransform(
                    $char,
                    static::offsetStep($offsetGenerator) * $mode
                ),
                \str_split(
                    static::normalize($text)
                )
            )
        );
    }

    public function encode(string $plainText): string
    {
        return $this->codec($plainText, 1);
    }

    public function decode(string $cipherText): string
    {
        return $this->codec($cipherText, -1);
    }
}
