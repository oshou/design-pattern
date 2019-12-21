<?php

class Gear
{
    private $chainring;
    private $cog;
    private $rim;
    private $tire;

    function __construct($chainring, $cog, $rim, $tire)
    {
        $this->chainring = $chainring;
        $this->cog = $cog;
        $this->rim = $rim;
        $this->tire = $tire;
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

    function rim()
    {
        return $this->rim;
    }

    function tire()
    {
        return $this->tire;
    }

    function gear_inches()
    {
        return $this->ratio() * ($this->rim + ($this->tire * 2));
    }
}

$gear1 = new Gear(52, 11, 26, 1.5);
echo $gear1->gear_inches() . PHP_EOL;

$gear2 = new Gear(52, 11, 24, 1.25);
echo $gear2->gear_inches() . PHP_EOL;
