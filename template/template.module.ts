import { Module } from '@nestjs/common';

import { $$TEMPLATE$$Controller } from './template.controller';
import { $$TEMPLATE$$Repository } from './template.repository';
import { $$TEMPLATE$$Service } from './template.service';

import { CustomTypeOrmModule } from '~/common/typeorm/custom-typeorm.module';

@Module({
  imports: [
    CustomTypeOrmModule.forFeature([$$TEMPLATE$$Repository], 'typeorm'),
  ],
  controllers: [$$TEMPLATE$$Controller],
  providers: [$$TEMPLATE$$Service],
  exports: [$$TEMPLATE$$Service, CustomTypeOrmModule],
})
export class $$TEMPLATE$$Module {}
