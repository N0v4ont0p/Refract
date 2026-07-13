> Source: https://raw.githubusercontent.com/FTCLib/FTCLib-Docs/v2.1.0/features/gamepad-extensions.md · Fetched: 2026-07-12
> Note: docs.ftclib.org (GitBook) returned HTTP 403 to automated fetch tools; content below is pulled from the FTCLib-Docs GitHub source at tag v2.1.0 (the same version live at https://docs.ftclib.org/ftclib/features/gamepad-extensions), which is the exact markdown GitBook renders for that page.

# Gamepad

The FTCLib provides enhanced Gamepad features. These classes are essentially extensions of the stock FTC SDK Gamepad features but with easier implementation methods.

## GamepadKeys

Provides enum representations of the buttons, D-Pad, bumpers, and triggers. Buttons, D-Pad, and bumpers are stored in `GamepadKeys.Button` and triggers are stored in `GamepadKeys.Trigger`.

| Buttons |
| :--- |
| Y |
| X |
| A |
| B |
| LEFT\_BUMPER |
| RIGHT\_BUMPER |
| BACK |
| START |
| DPAD\_UP |
| DPAD\_DOWN |
| DPAD\_LEFT |
| DPAD\_RIGHT |
| LEFT\_STICK\_BUTTON |
| RIGHT\_STICK\_BUTTON |

| Trigger |
| :--- |
| LEFT\_TRIGGER |
| RIGHT\_TRIGGER |

```java
// these are from the GamepadButton class that is used
// for command-based frameworks
GamepadButton grabButton = new GamepadButton(
    gamepad1, GamepadKeys.Button.A
);
GamepadButton releaseButton = new GamepadButton(
    gamepad2, GamepadKeys.Button.B
);

GamepadEx gamepadEx = new GamepadEx(gamepad1);
```

## GamepadEx

An extension of the stock FTC SDK `Gamepad` class. Constructed simply from a Gamepad. Provides six intuitive value-getting methods:

* `getButton()`: Given a `GamepadKeys.Button`, this method will check if that Button is pressed, returning a boolean of whether that Button is pressed.

```java
gamepadEx.getButton(GamepadKeys.Button.A);
```

* `getTrigger()`: Given a `GamepadKeys.Trigger`, this method will return the value of the Trigger (0 if unpressed, 1 if fully depressed).

```java
gamepadEx.getTrigger(GamepadKeys.Trigger.RIGHT_TRIGGER);
```

* `getLeftY()`: Returns the value of the y-axis of the left joystick (note that the value returned is the opposite of what would be returned from the standard gamepad object).

```java
gamepadEx.getLeftY();
```

* `getRightY()`: Returns the value of the y-axis of the right joystick

```java
gamepadEx.getRightY();
```

* `getLeftX()`: Returns the value of the x-axis of the left joystick

```java
gamepadEx.getLeftX();
```

* `getRightX()`: Returns the value of the x-axis of the right joystick

```text
gamepadEx.getRightX();
```

## KeyReader

The `KeyReader` interface is the base for objects that monitor an individual button or trigger on a gamepad. All `Reader` classes must implement these functions:

* `readValue()`: Reads the current value of the key, true or false, and updates the values used by the reader. Returns nothing. This must be called once every loop.
* `isDown()` : Checks if key is currently down. Will return a boolean of whether that key is pressed.
* `wasJustPressed()` : Returns boolean whether the key is pressed, but only if it was previously not pressed. 
* `wasJustReleased()` : Returns boolean indicating whether the key is not pressed, but only if it was previously pressed. 
* `stateJustChanged` : Returns boolean indicating that the key's value has switched.

## TriggerReader

The `TriggerReader` class implements the `KeyReader` interface. Because `GamepadEx` Triggers return a `double` , the `TriggerReader` class interprets a value of greater than `0.5` as a trigger press.

The following constructs a new Trigger Reader with a `GamepadEx` gamepad and `GamepadKeys.Trigger` trigger.

```java
TriggerReader triggerReader = new TriggerReader(
    gamepadEx, GamepadKeys.Trigger.RIGHT_TRIGGER
);
```

Below are the different methods you can use with the trigger reader.

```java
triggerReader.isDown();
triggerReader.readValue();
triggerReader.stateJustChanged();
triggerReader.wasJustPressed();
triggerReader.wasJustReleased();
```

## ButtonReader

The `ButtonReader`class implements the `KeyReader` interface. It checks if a button is pressed, released, or is down.

```java
ButtonReader reader = new ButtonReader(
    gamepadEx, GamepadKeys.Button.A
);
```

* `ButtonReader(GamepadEx gamepad, GamepadKeys.Button button)`: Constructs a new Button Reader with a `GamepadEx` gamepad and a `GamepadKeys.Button` button. 
* `ButtonReader(BooleanSupplier supplier)`: Constructs a new Button Reader using the value of a boolean supplier instead of a gamepad, which allows reading value states easily without a gamepad.

```java
reader.readValue();
reader.wasJustPressed();
reader.stateJustChanged();
reader.isDown();
reader.wasJustReleased();
```

The `GamepadEx` objects actually contain `ButtonReader`s. For every `GamepadKeys.Button`, there is a matching `ButtonReader` entry in the map. It is stored internally as a `Map<GamepadKeys.Button, ButtonReader>`. This allows you to use these features just with the `GamepadEx` class.

```java
// create the gamepad
GamepadEx myGamepad = new Gamepad(gamepad1);

/** The methods for using the ButtonReaders **/
myGamepad.wasJustPressed(GamepadKeys.Button.A);
myGamepad.stateJustChanged(GamepadKeys.Button.A);
myGamepad.isDown(GamepadKeys.Button.A);
myGamepad.wasJustReleased(GamepadKeys.Button.A);

// pass the GamepadKeys.Button that you want to read
// into the method argument

// to read all buttons at once, perform a single call
myGamepad.readButtons();
/*
this is the equivalent of calling readValue() once
for all your readers
*/
```

## ToggleButtonReader

```java
ToggleButtonReader toggleButtonReader = new ToggleButtonReader(
    gamepadEx, GamepadKeys.Button.A
);
```

The `ToggleButtonReader` class extends `ButtonReader` and adds the ability to get the status of a toggle. `readValue()` needs to be run in a loop to get the state of the toggle.

`getState()` : Gets the toggle value of a button or boolean supplier.

```java
toggleButtonReader.getState();
```

### Usage

```java
GamepadEx toolOp = new GamepadEx(gamepad2);
ToggleButtonReader aReader = new ToggleButtonReader(
  toolOp, GamepadKeys.Button.A
);

while (...) {
  if (aReader.getState()) {
    // if toggle state true
  } else {
    // if toggle state false
  }
  aReader.readValue();
}
```
