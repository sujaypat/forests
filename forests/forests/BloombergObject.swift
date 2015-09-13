//
//  BloombergObject.swift
//  forests
//
//  Created by Sujay Patwardhan on 9/13/15.
//  Copyright © 2015 bizzi-body. All rights reserved.
//

import Foundation

class BloombergObject : PFObject{
    @NSManaged var Name: String
    @NSManaged var ticker: String
    @NSManaged var value: String
    
    init(Name: String, ticker: String, value: String) {
        super.init()
        
        self.Name = Name
        self.ticker = ticker
        self.value = value
    }
    
    override init() {
        super.init()
    }
    
    override class func query() -> PFQuery? {
        //1
        let query = PFQuery(className: BloombergObject.parseClassName())
        //2
        query.includeKey("ticker")
        //3
        query.orderByDescending("value")
        return query
    }
    
    
}


extension BloombergObject: PFSubclassing {
    // Table view delegate methods here
    //1
    class func parseClassName() -> String {
        return "BloombergObject"
    }
    
    //2
    override class func initialize() {
        var onceToken: dispatch_once_t = 0
        dispatch_once(&onceToken) {
            self.registerSubclass()
        }
    }
}