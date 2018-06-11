<?php
srand(666 . time());

class Robot
{
    public $name;
    public static $pool = [];


    function __construct(){
        $this->setName();
    }

    function __destruct(){
        $this->reset();
    }

    public function getName(){
        return $this->name;
    }

    function randomName($tpl = "AADDD"){
        $name = "";
        $alpha = range("A","Z");

        foreach(str_split($tpl) as $k){
            $char = "";
            switch($k){
                case "A":
                    $char = $alpha[array_rand($alpha)];
                    break;
                case "D":
                    $char = rand(0,9);
                    break;
                default:
                    $char = $k;
            }
            $name .= $char;
        }

        return $name;
    }

    function setName(){
        $name = "";
        while(true){
            $name = $this->randomName();
            if(!isset(self::$pool[$name])){
                $this->name = $name;
                self::$pool[$name] = true ;
                break;
            }else{
                if(
                    count(self::$pool) >= ((26**2) * (10**3))
                ){
                    die("Too much name already taken this code not scale");
                }
            }
        }
    }

    function reset(){
        // unset(self::$pool[$this->name]); // Test don't want me to recycle the name …
        $this->setName();
    }
}
