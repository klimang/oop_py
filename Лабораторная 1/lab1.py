class ProgressBar:
    def __init__(self,start:int, end:int, text:str):
        """
        Initialize a progress bar builder with progress values and text.
        
        :param start: start progress value.
        :param end: maximum progress value.
        :param text: text of progress bar.
        
        Example:
        >>> bar = ProgressBar(0,100, "progress")
        """
        if start<0:
            raise ValueError("start value must be greater than zero")
        self.start:int=start
        if start<0:
            raise ValueError("end value must be greater than zero")
        self.end:int=end
        self.text:str=text
    def increment(self) -> None:
        """
        increment start value by 1.
        
        Example:
        >>> bar = ProgressBar(0,100, "progress")
        >>> bar.increment()
        """
        ...
    
    def update(self) -> None:
        """
        update progress bar and print it
        
        Example:
        >>> bar = ProgressBar(0,100, "progress")
        >>> bar.update()
        """
        ...
    
class Device:
    def __init__(self, brand: str, price: int):
        """
        Initialize a device with brand and price.
        
        :param brand: Brand of the device.
        :param price: price of the device.
        
        Example:
        >>> device = Device("ABC", 1000)
        """
        if not brand:
            raise ValueError("Brand should not be an empty string.")
        self.brand: str = brand

        if price < 0:
            raise ValueError("price should be a non-negative number.")
        self.price: int = price

    def sell(self,owner:str) -> None:
        """
        Sell the device.
        
        :param owner: new owner of the device.
        
        Example:
        >>> device = TechnicalDevice("ABC", 1000)
        >>> device.sell("JohnDoe")
        """
        ...

    def test(self) -> None:
        """
        test the device.
        
        Example:
        >>> device = TechnicalDevice("ABC", 1000)
        >>> device.test()
        """
        ...
        
class Image:
    def __init__(self,width:int,heght:int,data:list):
        """
        create image object with width, height and data
        
        param width:width of the image
        param height: height of the image
        param data: image content
        
        Example:
        >>> device = Image(500,500, data)
        >>> device.show()
        """
        if width<=0 and height<=0:
            raise ValueError("width and height must be greater than zero")
        self.width=width
        self.heght=heght
        if len(data)!=self.width*self.heght:
            raise ValueError("size of data must be equals width * height"
        self.data=data
        
    def show(self)->None:
        """
        shows the image
        
        Example:
        >>> device = Image(500,500, data)
        >>> device.show()
        """
        ...
        
    def get_dimensions()->(int,int):
        """
        return the width and height if the image

        :return: width and height.
        """
        ...