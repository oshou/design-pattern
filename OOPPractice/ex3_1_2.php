<?php
class Gear
{
    private $chainring;
    private $cog;
    private $wheel;

    function __construct($chainring, $cog, $wheel)
    {
        $this->chainring = $chainring;
        $this->cog = $cog;
        $this->wheel = $wheel;
    }

    // Accessor
    function chainring()
    {
        return $this->chainring;
    }

    function cog()
    {
        return $this->cog;
    }

    function wheel()
    {
        return $this->wheel;
    }

    function gear_inches()
    {
        $w = $this->wheel;
        return $this->ratio() * $w->diameter();
    }

    function ratio()
    {
        return $this->chainring() / $this->cog();
    }
}

class Wheel
{
    private $rim;
    private $tire;

    function __construct($rim, $tire)
    {
        $this->rim = $rim;
        $this->tire = $tire;
    }

    // Accessorメソッド
    function rim()
    {
        return $this->rim;
    }

    function tire()
    {
        return $this->tire;
    }

    function diameter()
    {
        return $this->rim() + ($this->tire() * 2);
    }
}

$w = new Wheel(26, 1.5);
$g = new Gear(52, 11, $w);
echo $g->gear_inches() . "\n";
