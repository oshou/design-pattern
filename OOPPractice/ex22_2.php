<?php
class Gear
{
    private $chainring;
    private $cog;

    function __construct($chainring, $cog)
    {
        $this->chainring = $chainring;
        $this->cog = $cog;
    }

    function ratio()
    {
        return $this->chainring / $this->cog;
    }

    function chainring()
    {
        return $this->chainring;
    }

    function cog()
    {
        return $this->cog;
    }
}

$gear1 = new Gear(52, 11);
echo $gear1->chainring() . PHP_EOL;
echo $gear1->cog() . PHP_EOL;
echo $gear1->ratio() . PHP_EOL;
$gear2 = new Gear(30, 27);
echo $gear2->chainring() . PHP_EOL;
echo $gear2->cog() . PHP_EOL;
echo $gear2->ratio() . PHP_EOL;
