<?php

class PhoneNumber{
    function __construct(string $phone){
        $clean = preg_replace("/\D/", "", $phone); # only digits

        // check for alpha in phone
        if(preg_match("/[[:alpha:]]/",$phone)){
            throw new InvalidArgumentException("Contains letter");
        }

        // check for country code
        $country_code = substr($clean,0,-10); # extract eventual country codes
        if($country_code === ''){ # if none default to 1
            $country_code = 1;
        }
        if($country_code != 1){
            throw new InvalidArgumentException("Invalid country code");
        }

        // the number itself
        $number = substr($clean,-10);
        $this->number = $number;
    }

    public function number(){
        return $this->number;
    }

    public function areaCode(){
        return substr($this->number,0,3);
    }

    public function prettyPrint(){
        return preg_replace(
            "/(\d{3})(\d{3})(\d{4})/",
            "($1) $2-$3",
            $this->number
        );
    }
}
